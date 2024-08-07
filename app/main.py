import sqlite3
import os
import argparse
import sys
from app.manager import generate_key, save_key, load_key, add_password, retrieve_password, list_passwords, generate_secure_password

# Función para inicializar la base de datos
def init_db():
    conn = sqlite3.connect('password_manager.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS passwords
                      (site TEXT PRIMARY KEY, password TEXT)''')
    conn.commit()
    conn.close()

def add_password_to_db(key, site, password):
    conn = sqlite3.connect('password_manager.db')
    cursor = conn.cursor()
    cursor.execute('INSERT OR REPLACE INTO passwords (site, password) VALUES (?, ?)', (site, password))
    conn.commit()
    conn.close()

def retrieve_password_from_db(site):
    conn = sqlite3.connect('password_manager.db')
    cursor = conn.cursor()
    cursor.execute('SELECT password FROM passwords WHERE site = ?', (site,))
    result = cursor.fetchone()
    conn.close()
    if result:
        return result[0]
    return None

def list_passwords_from_db():
    conn = sqlite3.connect('password_manager.db')
    cursor = conn.cursor()
    cursor.execute('SELECT site FROM passwords')
    sites = cursor.fetchall()
    conn.close()
    return [site[0] for site in sites]

def print_help():
    print("\nUsage:")
    print("  sudo psswrd [command]")
    print("\nCommands:")
    print("  add       - Add a new password")
    print("  retrieve  - Retrieve a password")
    print("  list      - List all stored passwords")
    print("  create    - Create and store a secure password for a site")

def main():
    # Verificar si el script se está ejecutando con sudo
    if os.geteuid() != 0:
        print("Este script debe ejecutarse con sudo.")
        sys.exit(1)

    parser = argparse.ArgumentParser(description='Password Manager CLI')
    parser.add_argument('command', nargs='?', default='help', help='Command to run')
    args = parser.parse_args()

    # Mostrar ayuda si se usa el comando 'help' o no se proporciona un comando
    if args.command == 'help' or args.command not in ['add', 'retrieve', 'list', 'create']:
        print_help()
        sys.exit(0)

    # Initialize the database
    init_db()

    # Load or generate the key
    key_file = 'key.key'
    if not os.path.exists(key_file):
        key = generate_key()
        save_key(key, key_file)
    else:
        key = load_key(key_file)

    # Handle commands
    if args.command == 'add':
        site = input("Enter the site name: ")
        password = input("Enter the password: ")
        add_password_to_db(key, site, password)
        print("Password added successfully!")

    elif args.command == 'retrieve':
        site = input("Enter the site name: ")
        password = retrieve_password_from_db(site)
        if password:
            print(f"The password for {site} is: {password}")
        else:
            print("Password not found.")

    elif args.command == 'list':
        sites = list_passwords_from_db()
        if sites:
            print("Stored passwords for sites:")
            for site in sites:
                print(site)
        else:
            print("No passwords stored.")

    elif args.command == 'create':
        site = input("Enter the site name: ")
        password = generate_secure_password()
        add_password_to_db(key, site, password)
        print(f"Secure password for {site} created and added successfully: {password}")

if __name__ == '__main__':
    main()
