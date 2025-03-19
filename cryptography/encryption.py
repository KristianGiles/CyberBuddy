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

print("\nWelcome to CyberBuddy's File Encryption Program!\n")
    
def load_file(): # Load the file from the current directory in read-only
    file_name = input("Enter the file you wish to encrypt: ")
    file_data = open(file_name, "rb").read()
    return file_data, file_name

def load_key(): #Loads the key from the current directory in read-only
    key_name = input("Enter the name of the encryption key you wish to use: ") 
    key = open(key_name, "rb").read() 
    return key

def generate_key_aes(): # Generate a key for AES and save it to a file
    # Generate a key for AES
    key = Fernet.generate_key()
    # Save the key to a file
    with open("aes_key.key", "wb") as key_file:
        key_file.write(key)
    return key

def encrypt_aes(file_data, file_name, key): # AES encryption using Fernet
    # Encrypting the data using a key
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(file_data)
    # Encrypt the file
    with open(file_name, "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)
    print("File created and written successfully!")

def generate_key_tripledes(): # Generate a key for Triple DES and save it to a file
    #Creating a 16 byte key for Triple DES using 16 random bytes
    key = os.urandom(16)
    #Saving the key to a file
    with open("tripledes_key.key", "wb") as key_file:
        key_file.write(key)
    return key
    pad_length = data[-1] # The last byte determines if the data is padded
    return data[:-pad_length]

def encrypt_tripledes(file_data, file_name, key): # Triple DES encryption using ECB mode which does not use IVs
    # Encrypt the data using Triple DES in ECB mode, IVs are not used in ECB mode so they are set to nothing
    cipher = DES3.new(key, DES3.MODE_ECB)
    padded_data = pad(file_data, 8)
    encrypted_data = cipher.encrypt(padded_data)
    # Write the encrypted data to a file
    with open(file_name, "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)
    print("File encrypted successfully!")

def encrypt_rsa():
    # RSA encryption
    pass

def encrypt_ecc():
    # Elliptic Curve Cryptography encryption
    pass

def generate_key_rsa():
    # RSA key generation
    pass

def generate_key_ecc():
    # Elliptic Curve Cryptography key generation
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
                key = generate_key_tripledes()
            elif user_choice == "3":
                key = generate_key_rsa()
            elif user_choice == "4":
                key = generate_key_ecc()
            break
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")

    if user_choice == "1":
        encrypt_aes(file_data, file, key)
    elif user_choice == "2":
        encrypt_tripledes(file_data, file, key)
    elif user_choice == "3":
        encrypt_rsa()
    elif user_choice == "4":
        encrypt_ecc()
    else:
        print("Invalid input. Please try again.")
        
__main__()
#run the program