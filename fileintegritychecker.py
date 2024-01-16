# Author: Craig Ferguson
# 01/14/2024
# File integrity checker tool

import hashlib
import os

def calculate_file_hash(file_path, block_size=65536):
    """Calculate the hash of a file."""
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as file:
        buffer = file.read(block_size)
        while len(buffer) > 0:
            hasher.update(buffer)
            buffer = file.read(block_size)
    return hasher.hexdigest()

def save_hash_to_file(file_path, hash_value):
    """Save the hash value to a file."""
    with open(file_path, 'w') as hash_file:
        hash_file.write(hash_value)

def read_hash_from_file(file_path):
    """Read the hash value from a file."""
    with open(file_path, 'r') as hash_file:
        return hash_file.read()

def check_integrity(file_path, hash_file_path):
    """Check the integrity of a file."""
    if not os.path.isfile(file_path):
        print("Error: File not found.")
        return False

    if not os.path.isfile(hash_file_path):
        print("Error: Hash file not found. Run the initial hash calculation first.")
        return False

    stored_hash = read_hash_from_file(hash_file_path)
    current_hash = calculate_file_hash(file_path)

    if stored_hash == current_hash:
        print("File integrity is intact.")
        return True
    else:
        print("File integrity check failed. The file has been modified.")
        return False

# Example usage:
file_to_check = 'example.txt'
hash_file = 'hash.txt'

# Calculate and save the initial hash
hash_value = calculate_file_hash(file_to_check)
save_hash_to_file(hash_file, hash_value)

# Check integrity later
check_integrity_result = check_integrity(file_to_check, hash_file)
