import os.path
import json
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Define the scopes required for the Google Drive API.
# 'https://www.googleapis.com/auth/drive.metadata.readonly' allows read-only access to file metadata.
SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']

# Name of the file to store user credentials.
TOKEN_FILE = 'token.json'
# Name of the file containing OAuth 2.0 client secrets.
CREDENTIALS_FILE = 'credentials.json'
# Name of the output file for storing drive activity.
OUTPUT_FILE = 'google_drive_activity.json'

# SCOPES needs to be updated to include drive.readonly for exporting files
# Old: SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']
SCOPES = ['https://www.googleapis.com/auth/drive.readonly'] # drive.readonly includes metadata and file content access

def get_google_doc_content_as_text(drive_service, file_id: str) -> str | None:
    """
    Downloads a Google Document identified by file_id as plain text.

    Args:
        drive_service: An authorized Google Drive API service instance.
        file_id: The ID of the Google Document to download.

    Returns:
        The content of the Google Document as a plain text string, 
        or None if an error occurs or the file is not a Google Doc.
    """
    try:
        # First, get file metadata to confirm it's a Google Doc, as export only works for Google Docs.
        # Other Google Workspace types (Sheets, Slides) need different export MIME types.
        # For this function, we focus on Google Docs -> text/plain.
        file_metadata = drive_service.files().get(fileId=file_id, fields='mimeType, name').execute()
        if file_metadata.get('mimeType') == 'application/vnd.google-apps.document':
            request = drive_service.files().export_media(fileId=file_id, mimeType='text/plain')
            response_bytes = request.execute()
            return response_bytes.decode('utf-8')
        else:
            print(f"File '{file_metadata.get('name')}' (ID: {file_id}) is not a Google Document (mimeType: {file_metadata.get('mimeType')}). Cannot export as plain text.")
            return None
    except HttpError as error:
        print(f"An API error occurred while trying to export file ID {file_id}: {error}")
        print(f"Details: {error.resp.status} - {error._get_reason()}")
        if error.resp.status == 403:
            print("This could be due to insufficient permissions. Ensure the 'drive.readonly' scope was granted.")
        elif error.resp.status == 404:
            print(f"File with ID {file_id} not found.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred while exporting file ID {file_id}: {e}")
        return None

def get_authenticated_drive_service():
    """
    Authenticates with Google Drive API and returns the service object.
    This function encapsulates the authentication logic from the original main().
    """
    creds = None
    if os.path.exists(TOKEN_FILE):
        try:
            creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
        except ValueError as e: # Handle malformed token.json
            print(f"Error loading token from '{TOKEN_FILE}': {e}. Will attempt to re-authenticate.")
            creds = None # Force re-authentication
            if os.path.exists(TOKEN_FILE): # Remove invalid token file
                 os.remove(TOKEN_FILE)


    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            try:
                creds.refresh(Request())
            except Exception as e:
                print(f"Error refreshing token: {e}. Deleting potentially corrupt '{TOKEN_FILE}' and re-authenticating.")
                if os.path.exists(TOKEN_FILE):
                    os.remove(TOKEN_FILE) # Remove problematic token
                flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
                creds = flow.run_local_server(port=0)
        else:
            if not os.path.exists(CREDENTIALS_FILE):
                print(f"Error: '{CREDENTIALS_FILE}' not found.")
                print("Please download your OAuth 2.0 client credentials from the Google Cloud Console")
                print("and place it in the same directory as this script.")
                return None
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        
        with open(TOKEN_FILE, 'w') as token:
            token.write(creds.to_json())
            print(f"Authentication successful. Token saved to '{TOKEN_FILE}'")
    
    try:
        return build('drive', 'v3', credentials=creds)
    except HttpError as error:
        print(f"Failed to build Drive service: {error}")
        return None


def main():
    """
    Fetches metadata of the 20 most recently modified files from Google Drive
    and stores it in a local JSON file.
    """
    """
    Fetches metadata of the 20 most recently modified files from Google Drive
    and stores it in a local JSON file.
    """
    service = get_authenticated_drive_service()
    if not service:
        print("Could not authenticate with Google Drive. Exiting.")
        return

    try:

        # Fetch the 20 most recently modified files.
        # 'orderBy' sorts files by their last modification time in descending order.
        # 'pageSize' limits the number of results.
        # 'fields' specifies which file metadata properties to retrieve.
        # Added 'webViewLink' to provide a direct link to the file in the Drive UI.
        results = service.files().list(
            orderBy='modifiedTime desc',
            pageSize=20, # Fetch a few more in case the first one is not a Google Doc
            fields="nextPageToken, files(id, name, mimeType, modifiedTime, webViewLink)"
        ).execute()

        items = results.get('files', [])

        if not items:
            print('No files found.')
            drive_activity_list = [] # Renamed to avoid conflict with local var in main example
        else:
            print('Recently modified files (metadata will be saved):')
            drive_activity_list = []
            for item in items:
                file_metadata = {
                    'id': item['id'],
                    'name': item['name'],
                    'mimeType': item['mimeType'],
                    'modifiedTime': item['modifiedTime'],
                    'webViewLink': item.get('webViewLink') # Get webViewLink if available
                }
                drive_activity_list.append(file_metadata)
                print(f"- {item['name']} (ID: {item['id']}, Type: {item['mimeType']}, Last Modified: {item['modifiedTime']})")

        # Store the fetched metadata in a JSON file.
        with open(OUTPUT_FILE, 'w') as outfile:
            json.dump(drive_activity_list, outfile, indent=4)
        print(f"\nSuccessfully fetched and stored activity metadata in '{OUTPUT_FILE}'")

    except HttpError as error:
        print(f'An API error occurred while listing files: {error}')
        print(f"Details: {error.resp.status} - {error._get_reason()}")
        if error.resp.status == 403:
            print("This might be due to the Drive API not being enabled or insufficient scopes.")
            print("Ensure the Google Drive API is enabled: https://console.cloud.google.com/apis/library/drive.googleapis.com")
            print(f"Current scopes used: {SCOPES}")
        elif error.resp.status == 401:
             print("Authentication error. Try deleting '{TOKEN_FILE}' and re-authenticating.")
    except FileNotFoundError as e:
        # This should be caught by get_authenticated_drive_service if credentials.json is missing
        print(f"A file was not found: {e}")
    except Exception as e:
        print(f"An unexpected error occurred in main(): {e}")

if __name__ == '__main__':
    # Example of how to use the new function (optional, can be removed or kept for direct testing)
    # This part is primarily for testing fetch_drive_activity.py itself.
    # The run_integration_test.py will call main() and then get_google_doc_content_as_text()
    
    main() # Fetch and save metadata first
    
    # Example: try to get content of the first Google Doc found in the output file
    if os.path.exists(OUTPUT_FILE):
        with open(OUTPUT_FILE, 'r') as f:
            activity = json.load(f)
        
        first_google_doc_id = None
        first_google_doc_name = None
        if activity:
            for item_activity in activity:
                if item_activity['mimeType'] == 'application/vnd.google-apps.document':
                    first_google_doc_id = item_activity['id']
                    first_google_doc_name = item_activity['name']
                    break # Found one
        
        if first_google_doc_id:
            print(f"\nAttempting to fetch content for the first Google Doc found: '{first_google_doc_name}' (ID: {first_google_doc_id})")
            # Need to re-authenticate or pass the service object
            drive_service = get_authenticated_drive_service()
            if drive_service:
                content = get_google_doc_content_as_text(drive_service, first_google_doc_id)
                if content:
                    print(f"\n--- Content of '{first_google_doc_name}' ---")
                    print(content[:500] + "..." if len(content) > 500 else content)
                    print("--- End of content ---")
                else:
                    print(f"Could not retrieve content for '{first_google_doc_name}'.")
            else:
                print("Could not get authenticated Google Drive service to fetch document content.")
        else:
            print("\nNo Google Docs found in the first 20 recently modified files to test content fetching.")
