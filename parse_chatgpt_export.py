import json
import os
import sys
import argparse

def parse_message(message_data):
    """
    Extracts relevant information from a single message within a conversation.
    """
    if not message_data or "message" not in message_data or not message_data["message"]:
        return None

    message = message_data["message"]
    author_role = message.get("author", {}).get("role", "unknown")
    content_parts = message.get("content", {}).get("parts", [])
    
    text_content = ""
    if content_parts and isinstance(content_parts, list) and content_parts[0] and isinstance(content_parts[0], str):
        text_content = content_parts[0] # Assuming text content is always the first part and a simple string
    elif content_parts and isinstance(content_parts, dict) and "text" in content_parts: # Fallback for older format?
        text_content = content_parts.get("text","")


    if author_role == "user":
        return f"User: {text_content}"
    elif author_role == "assistant":
        return f"Assistant: {text_content}"
    elif author_role == "system": # System messages (e.g. instructions, model information)
        return f"System: {text_content}"
    return None


def main(export_folder_path):
    """
    Parses conversations.json from a ChatGPT export folder and saves extracted data.
    """
    conversations_file_path = os.path.join(export_folder_path, 'conversations.json')

    if not os.path.exists(conversations_file_path):
        print(f"Error: 'conversations.json' not found in '{export_folder_path}'")
        print("Please ensure you provide the correct path to the unzipped ChatGPT export folder.")
        return

    try:
        with open(conversations_file_path, 'r', encoding='utf-8') as f:
            try:
                all_conversations_data = json.load(f)
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON from '{conversations_file_path}': {e}")
                return
    except IOError as e:
        print(f"Error reading file '{conversations_file_path}': {e}")
        return

    extracted_conversations = []

    for convo_data in all_conversations_data:
        if not isinstance(convo_data, dict):
            print(f"Skipping non-dictionary item in conversations list: {convo_data}")
            continue

        convo_id = convo_data.get('id')
        title = convo_data.get('title', 'Untitled')
        create_time = convo_data.get('create_time')
        
        messages_concat = []
        
        # The actual conversation messages are nested under 'mapping'
        mapping = convo_data.get('mapping', {})
        
        # Iterate through messages, sort them by create_time if available or assume order
        # For simplicity, we'll process messages as they appear if no create_time in node
        # A more robust solution might involve building a tree and traversing it by 'children'
        
        current_node_id = None
        # Find the root message node (the one with no parent)
        for node_id, node_data in mapping.items():
            if node_data and node_data.get("parent") is None and node_data.get("message"):
                 # Check if this is a root of a new system message based conversation (without title)
                if node_data["message"].get("author",{}).get("role") == "system" and \
                   node_data["message"].get("metadata",{}).get("user_context_message_data"):
                    # This seems to be a system message starting a new conversation variant
                    # often seen in newer exports where title might be under this system message.
                    # Try to get title from here if main title is None or generic
                    if title == 'Untitled' or title is None:
                         title = node_data["message"]["metadata"]["user_context_message_data"].get("title", title)

                # Heuristic: if we have a root message, start from there.
                # Some exports might have multiple "root" nodes if the structure is complex or varies.
                # This simple parser will pick the first one it finds.
                # A more complex parser might need to handle branching/multiple roots differently.
                if current_node_id is None or (mapping[current_node_id].get("message") is None and node_data.get("message") is not None) :
                    current_node_id = node_id


        processed_messages_in_convo = set()
        
        # Traverse the conversation from the identified root (or first node if no clear root)
        # This loop attempts to follow the children pointers to reconstruct order
        # It's a simplification; true chronological order relies on message create_time within nodes.
        
        # Find the actual first message node
        # The root node itself might not have a message, but points to the first message.
        # Or, the first message is the root node.
        
        # Try to find the earliest message node if simple root finding fails
        if not current_node_id and mapping:
             # Fallback: if no clear root, pick the one with the smallest ID (often the start)
             # or the one with the earliest timestamp if available in 'message.create_time'
            potential_starts = []
            for node_id_iter, node_data_iter in mapping.items():
                if node_data_iter and node_data_iter.get("message"):
                    msg_create_time = node_data_iter["message"].get("create_time")
                    if msg_create_time:
                        potential_starts.append((msg_create_time, node_id_iter))
                    else: # if no create_time, use id as a proxy (less reliable)
                         potential_starts.append((float('inf'), node_id_iter)) # put ones without time last
            if potential_starts:
                potential_starts.sort()
                current_node_id = potential_starts[0][1]


        while current_node_id and current_node_id in mapping and current_node_id not in processed_messages_in_convo:
            node = mapping[current_node_id]
            if not node: # Should not happen if ID is in mapping
                break
            
            processed_messages_in_convo.add(current_node_id)
            parsed_msg = parse_message(node) # node itself contains the message data
            if parsed_msg:
                messages_concat.append(parsed_msg)

            # Move to the next message - this assumes a linear sequence via children
            # ChatGPT conversations can branch. This script takes the first child.
            children_nodes = node.get('children', [])
            if children_nodes:
                current_node_id = children_nodes[0] # Take the first child to follow a path
            else:
                current_node_id = None # End of this path

        if messages_concat: # Only add conversation if it has messages
            extracted_conversations.append({
                "id": convo_id,
                "title": title,
                "create_time": create_time,
                "messages": "\n".join(messages_concat)
            })
        elif not title or title == "Untitled":
             print(f"Skipping conversation with ID {convo_id} as it has no messages and no meaningful title.")


    output_file_path = 'chatgpt_conversations.json'
    try:
        with open(output_file_path, 'w', encoding='utf-8') as outfile:
            json.dump(extracted_conversations, outfile, indent=2)
        print(f"\nSuccessfully parsed conversations.")
        print(f"Extracted data saved to '{output_file_path}'")
    except IOError as e:
        print(f"Error writing output file '{output_file_path}': {e}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Parse ChatGPT export data.")
    parser.add_argument("export_folder_path", type=str,
                        help="Path to the unzipped ChatGPT export folder (containing conversations.json)")
    args = parser.parse_args()
    main(args.export_folder_path)
