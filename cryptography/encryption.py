from cryptography.fernet import Fernet #pip3 install cryptography
from M2Crypto.EVP import Cipher
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

print("\nWelcome to CyberBuddy's File Encryption Program!\n")
    
def load_file():
    # Load the file from the current directory in read-only
    file_name = input("Enter the file you wish to encrypt: ")
    file_data = open(file_name, "rb").read()
    return file_data, file_name

def load_key():
    # Load the key from the current directory in read-only
    key_name = input("Enter the name of they key: ") 
    key = open(key_name, "rb").read() 
    return key

def encrypt_aes(file_data, file_name): 
    # AES encryption using Fernet
    
    user_input = input("Do you have a key to use? (Y/N): ")
    if user_input in ["Y", "y", "Yes", "yes"]:
        # Load the key from the key function
        key = load_key()
        
    elif user_input in ["N", "n", "No", "no"]:
        # Generate a key for AES and save it to a file
        key = Fernet.generate_key()
        with open("aes_key.key", "wb") as key_file:
            key_file.write(key)
    else:
        print("Invalid input. Please try again.")
        encrypt_aes(file_data, file_name)
    # Encrypting the data using a key
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(file_data)
    
    # Encrypt the file
    with open(file_name, "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)
    print("File created and written successfully!")

def encrypt_tripledes():
    # Triple DES encryption
    user_input = input("Do you have a key to use? (Y/N): ")
    if user_input in ["Y", "y", "Yes", "yes"]:
        # Load the key from the key function
        key = load_key()
        
    elif user_input in ["N", "n", "No", "no"]:
        #Creating a 16 byte key for Triple DES using 16 random bytes
        key = os.urandom(16)
    else:
        print("Invalid input. Please try again.")
        encrypt_tripledes()
    
    
        
def encrypt_rsa():
    # RSA encryption
    pass

def encrypt_ecc():
    # Elliptic Curve Cryptography encryption
    pass

def __main__():
    file_data, file = load_file()
    # Load the file from the current directory to be used against an encryption algorithm
    
    #If user choice is AES, then encrypt the file with encrypt_aes
    encrypt_aes(file_data, file)
    
__main__()
#run the program