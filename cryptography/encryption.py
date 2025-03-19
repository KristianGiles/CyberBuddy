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
    key_name = input("Enter the name of the encryption key you wish to use: ") 
    key = open(key_name, "rb").read() 
    return key

def generate_key_aes():
    # Generate a key for AES and save it to a file
    key = Fernet.generate_key()
    with open("aes_key.key", "wb") as key_file:
        key_file.write(key)
    return key

def encrypt_aes(file_data, file_name): 
    # AES encryption using Fernet
    
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
    print("What encryption algorithm would you like to use?")
    print("1. AES")
    print("2. Triple DES")
    print("3. RSA")
    print("4. ECC")
    user_choice = input("Enter the number of the encryption algorithm you wish to use: ")

    file_data, file = load_file()
    # Load the file from the current directory to be used against an encryption algorithm

    while True:
    # Loop the prompt until a valid input is given
        user_input = input("Do you have a key to use? (Y/N): ")
        if user_input in ["Y", "y", "Yes", "yes"]:
            #Load the key from the key function if the user has a key
            key = load_key()
            break
        elif user_input in ["N", "n", "No", "no"]:
            # Generate a key if the user does not have one. The key is based on the encryption algorithm chosen at the start
            if user_choice == "1":
                key = generate_key_aes()
            elif user_choice == "2":
                key = encrypt_tripledes()
            elif user_choice == "3":
                key = encrypt_rsa()
            elif user_choice == "4":
                key = encrypt_ecc()
            break
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")

__main__()
#run the program