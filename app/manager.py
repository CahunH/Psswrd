from cryptography.fernet import Fernet
import os
import json

def generate_key():
    return Fernet.generate_key()

def save_key(key, filename='key.key'):
    with open(filename, 'wb') as key_file:
        key_file.write(key)

def load_key(filename='key.key'):
    with open(filename, 'rb') as key_file:
        return key_file.read()

def encrypt_password(key, password):
    fernet = Fernet(key)
    encrypted_password = fernet.encrypt(password.encode())
    return encrypted_password

def decrypt_password(key, encrypted_password):
    fernet = Fernet(key)
    decrypted_password = fernet.decrypt(encrypted_password).decode()
    return decrypted_password

def add_password(key, site, password, filename='passwords.json'):
    encrypted_password = encrypt_password(key, password)
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            passwords = json.load(file)
    else:
        passwords = {}
    passwords[site] = encrypted_password.decode()
    with open(filename, 'w') as file:
        json.dump(passwords, file)

def retrieve_password(key, site, filename='passwords.json'):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            passwords = json.load(file)
        encrypted_password = passwords.get(site)
        if encrypted_password:
            return decrypt_password(key, encrypted_password.encode())
        else:
            return None
    else:
        return None

def list_passwords(filename='passwords.json'):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            passwords = json.load(file)
        return list(passwords.keys())
    else:
        return []
