#!/bin/bash

# Script to bootstrap the social media automation infrastructure

# --- Configuration ---
# If you have a fixed N8N encryption key you want to use, set it here.
# Otherwise, the docker-compose.yml will use its default or you'll be prompted.
# N8N_ENCRYPTION_KEY="your_super_secret_encryption_key_here_please_change_me"

# Preferred timezone for N8N
GENERIC_TIMEZONE="America/New_York" # Change to your timezone, e.g., Europe/Berlin, Asia/Kolkata

# --- Helper Functions ---
print_info() {
    echo "INFO: $1"
}

print_success() {
    echo "SUCCESS: $1"
}

print_warning() {
    echo "WARNING: $1"
}

print_error() {
    echo "ERROR: $1"
    exit 1
}

check_command() {
    if ! command -v $1 &> /dev/null; then
        print_error "$1 could not be found. Please install it and try again."
    fi
}

# --- Pre-flight Checks ---
print_info "Performing pre-flight checks..."
check_command docker
check_command docker-compose
print_success "Docker and docker-compose are installed."

# --- Directory Setup ---
print_info "Setting up directories..."
if [ ! -d "./puppeteer_scripts" ]; then
    print_info "Creating directory ./puppeteer_scripts for Puppeteer scripts."
    mkdir ./puppeteer_scripts
else
    print_info "./puppeteer_scripts directory already exists."
fi

if [ ! -f "./puppeteer_scripts/postToLinkedIn.js" ]; then
    print_warning "./puppeteer_scripts/postToLinkedIn.js not found. Make sure to add your Puppeteer scripts there."
    # You could also choose to automatically download/create a placeholder:
    # echo "console.log('Placeholder Puppeteer script');" > ./puppeteer_scripts/postToLinkedIn.js
    # print_info "Created a placeholder postToLinkedIn.js. Please replace it with your actual script."
fi

if [ ! -f "./docker-compose.yml" ]; then
    print_error "./docker-compose.yml not found. This script expects it to be in the current directory."
fi

if [ ! -f "./n8n_starter_flow.json" ]; then
    print_warning "./n8n_starter_flow.json not found. You'll need to import this into N8N manually."
fi


# --- Environment Variables ---
# Set N8N_ENCRYPTION_KEY if not already set in the environment
if [ -z "$N8N_ENCRYPTION_KEY" ]; then
    # You can prompt for it, or use a default from docker-compose.yml, or generate one.
    # For this script, we'll rely on the default in docker-compose.yml or one set externally.
    print_warning "N8N_ENCRYPTION_KEY is not set in this script. Ensure it's set in your environment or docker-compose.yml, or change the default in docker-compose.yml."
    print_warning "Using the default from docker-compose.yml (which might be insecure if not changed)."
else
    export N8N_ENCRYPTION_KEY
    print_info "N8N_ENCRYPTION_KEY will be used from this script's configuration."
fi

if [ -z "$GENERIC_TIMEZONE" ]; then
    print_warning "GENERIC_TIMEZONE is not set. N8N will use its default (Europe/Berlin) or what's in docker-compose.yml."
else
    export GENERIC_TIMEZONE
    print_info "GENERIC_TIMEZONE set to $GENERIC_TIMEZONE."
fi


# --- Docker Compose ---
print_info "Starting services using Docker Compose..."
# The -d flag runs containers in detached mode.
# Use `docker-compose logs -f` to see logs.
# Use `docker-compose down` to stop services.

# The `export` commands above make these variables available to docker-compose
docker-compose up -d --build

if [ $? -eq 0 ]; then
    print_success "Docker containers should be starting up."
    print_info "N8N should be available at http://localhost:5678 (or your server's IP if running remotely)."
    print_info "To check logs: docker-compose logs -f"
    print_info "To stop services: docker-compose down"
    print_info "Remember to:"
    print_info "1. Change the default N8N_ENCRYPTION_KEY in docker-compose.yml or your environment for security."
    print_info "2. Import the n8n_starter_flow.json into your N8N instance."
    print_info "3. Place your actual Puppeteer scripts (like postToLinkedIn.js) in the ./puppeteer_scripts directory."
    print_info "4. Configure GitHub webhooks to point to your N8N instance."
else
    print_error "Docker Compose failed to start. Check the output above for errors."
fi

echo ""
print_success "Bootstrap script finished."
