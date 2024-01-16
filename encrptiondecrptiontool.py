# Author: Craig Ferguson
# 01/14/2024
# encryption/decrytion tool.

from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def save_key(key, filename):
    with open(filename, 'wb') as key_file:
        key_file.write(key)

def load_key(filename):
    return open(filename, 'rb').read()

def encrypt_file(key, input_file, output_file):
    cipher = Fernet(key)
    with open(input_file, 'rb') as file:
        file_data = file.read()
        encrypted_data = cipher.encrypt(file_data)
    with open(output_file, 'wb') as file:
        file.write(encrypted_data)

def decrypt_file(key, input_file, output_file):
    cipher = Fernet(key)
    with open(input_file, 'rb') as file:
        encrypted_data = file.read()
        decrypted_data = cipher.decrypt(encrypted_data)
    with open(output_file, 'wb') as file:
        file.write(decrypted_data)

# Example usage
key = generate_key()
save_key(key, 'secret.key')

encrypt_file(key, 'plaintext.txt', 'encrypted.txt')

# To decrypt
loaded_key = load_key('secret.key')
decrypt_file(loaded_key, 'encrypted.txt', 'decrypted.txt')
