<<<<<<< HEAD:cryptography/decryption.py
from cryptography.fernet import Fernet # pip3 install cryptography
from Crypto.Cipher import DES3, PKCS1_OAEP # pip3 install pycryptodome or python3 -m pip install --upgrade --no-cache-dir pycryptodome
from Crypto.Util.Padding import unpad
from Crypto.PublicKey import RSA 
=======
from cryptography.fernet import Fernet 
from Crypto.Cipher import DES3 
from Crypto.Util.Padding import pad, unpad
>>>>>>> efa6e218b925b4d6d3abbd8e0bc756b8f325d85c:crypto/decryption.py
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
print("     / C-Buddy \\     ")
print("    /___________\\    ")

print("\nWelcome to CyberBuddy's File Decryption Program!\n")

def load_file():
    # Load the file from the current directory in read-only
    file_name = input("Enter the file you wish to decrypt: ")
    file_data = open(file_name, "rb").read()
    return file_data, file_name

def load_key(): # Load the key from the current directory in read-only
    key_name = input("Enter the name of they key: ") 
    key = open(key_name, "rb").read()
    return key

def load_private_key(): # Load the private key from the current directory in read-only
    key_name = input("Enter the name of the private key: ")
    with open(key_name, "rb") as private_file:
        # Imports the key to a readable format
        private_key = RSA.import_key(private_file.read())
    print("Private key loaded successfully!")
    return private_key

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
    
def decrypt_rsa(file_data, file_name, private_key):
    cipher_rsa = PKCS1_OAEP.new(private_key)
    decrypted_data = cipher_rsa.decrypt(file_data)
    with open(file_name, "wb") as decrypted_file:
        decrypted_file.write(decrypted_data)
    print("File decrypted successfully!")

def decrypt_ecc():
    pass

def __main__():
    print("What decryption algorithm would you like to use?")
    print("1. AES")
    print("2. Triple DES")
    print("3. RSA")
    print("4. ECC")
    user_choice = input("Enter the number of the decryption algorithm you wish to use: ")
    
    # Load the file and key
    file_data, file_name = load_file()
    
    # Decrypt the file based on the user's choice
    if user_choice == "1":
        key = load_key()
        decrypt_aes(file_data, file_name, key)
    elif user_choice == "2":
        key = load_key()
        decrypt_tripledes(file_data, file_name, key)
    elif user_choice == "3":
        private_key = load_private_key()
        decrypt_rsa(file_data, file_name, private_key)
    elif user_choice == "4":
        decrypt_ecc()
    else:
        print("Invalid input. Please try again.")
    
__main__()