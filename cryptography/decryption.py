from cryptography.fernet import Fernet # pip3 install cryptography
from Crypto.Cipher import DES3 # pip3 install pycryptodome or python3 -m pip install --upgrade --no-cache-dir pycryptodome
from Crypto.Util.Padding import pad, unpad
import os

print("        *****        ")
print("      *       *      ")
print("    *  ^     ^  *    ")
print("   *     \\_/     *   ")
print("   *             *   ")
print("    *           *    ")
print("      *       *      ")
print("        *****        ")
print("      /       \\      ")
print("     / WELCOME \\     ")
print("    /___________\\    ")

print("\nWelcome to CyberBuddy's File Decryption Program!\n")

def load_file():
    # Load the file from the current directory in read-only
    file_name = input("Enter the file you wish to decrypt: ")
    file_data = open(file_name, "rb").read()
    return file_data, file_name

def load_key():
    # Load the key from the current directory in read-only
    key_name = input("Enter the name of they key: ") 
    key = open(key_name, "rb").read()
    return key
    
def decrypt_aes(file_data, file_name, key): # AES decryption using Fernet
    f = Fernet(key)
    # decrypt data
    decrypted_data = f.decrypt(file_data)
    # write the original file
    with open(file_name, "wb") as file:
        file.write(decrypted_data)
    
    print("File decrypted successfully!")
    
def decrypt_tripledes(file_data, file_name, key):
    decipher = DES3.new(key, DES3.MODE_ECB)
    decrypted_padded = decipher.decrypt(file_data)
    decrypted_data = unpad(decrypted_padded, 8)
    with open(file_name, "wb") as file:
        file.write(decrypted_data)
    print("File decrypted successfully!")
    
def __main__():
    file_data, file = load_file()
    key = load_key()
    decrypt_tripledes(file_data, file, key)
    
__main__()
