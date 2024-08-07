from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import secrets
import string

def generate_key():
    return secrets.token_bytes(32)

def save_key(key, filename='key.key'):
    with open(filename, 'wb') as key_file:
        key_file.write(key)

def load_key(filename='key.key'):
    with open(filename, 'rb') as key_file:
        return key_file.read()

def encrypt_password(key, password):
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(password.encode(), AES.block_size))
    return cipher.iv + ct_bytes

def decrypt_password(key, encrypted_password):
    iv = encrypted_password[:16]
    ct = encrypted_password[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct), AES.block_size)
    return pt.decode()

def add_password(key, site, password, filename='passwords.json'):
    encrypted_password = encrypt_password(key, password)
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            passwords = json.load(file)
    else:
        passwords = {}
    passwords[site] = encrypted_password.hex()
    with open(filename, 'w') as file:
        json.dump(passwords, file)

def retrieve_password(key, site, filename='passwords.json'):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            passwords = json.load(file)
        encrypted_password = passwords.get(site)
        if encrypted_password:
            return decrypt_password(key, bytes.fromhex(encrypted_password))
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

def generate_secure_password(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for i in range(length))
    return password
