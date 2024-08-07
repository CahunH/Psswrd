# Password Manager CLI

This README provides instructions on how to install the Password Manager CLI application as an executable, use it, and uninstall it.

## Overview

The Password Manager CLI is a command-line tool for securely managing passwords. It stores passwords in an SQLite database and encrypts them using a generated key.

## Installation

### 1. Clone the Repository

Clone the repository to your local machine:

    git clone https://github.com/yourusername/password-manager-cli.git
    cd password-manager-cli


### 2. Set Up a Python Virtual Environment

Create and activate a virtual environment:

    python3 -m venv venv
    source venv/bin/activate  # On Linux and macOS
    

### 3. Install Required Packages

Install the necessary Python packages:

    pip install -r requirements.txt

### 4. Install PyInstaller

PyInstaller is used to create the executable. Install it in your virtual environment:

    pip install pyinstaller

    pip install pycryptodome

### 5. Create the Executable

Generate the executable using PyInstaller:

    pyinstaller --onefile --name psswrd app/main.py

This will create an executable file named `psswrd` in the `dist` directory.

### 6. Move the Executable to a Directory in Your PATH

For easier access, move the executable to a directory in your PATH:

    sudo mv dist/psswrd /usr/local/bin/

### 7. Ensure Executable Permissions

Ensure the executable has the correct permissions:

    sudo chmod +x /usr/local/bin/psswrd

## Usage

Run the application with `sudo` to execute commands:

    sudo psswrd [command]

### Available Commands

- `add`: Add a new password.
- `retrieve`: Retrieve a stored password.
- `list`: List all stored passwords.
- `help`: Show help information.

## Uninstallation

### 1. Remove the Executable

To remove the executable, run:

    sudo rm /usr/local/bin/psswrd

### 3. Clean Up Python Packages

If you no longer need the Python packages, you can uninstall them:

    pip uninstall -r requirements.txt
