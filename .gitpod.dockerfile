FROM gitpod/workspace-full:latest

# Update packages and install SQLite and python3-venv
RUN sudo apt-get update && \
    sudo apt-get upgrade -y && \
    sudo apt-get install -y sqlite3 libsqlite3-dev python3-venv
