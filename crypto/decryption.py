from cryptography.fernet import Fernet 
from Crypto.Cipher import DES3 
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
    
def decrypt_rsa():
    pass

def decrypt_ecc():
    pass

def __main__():
    print("What decryption algorithm would you like to use?")
    print("1. AES")
    print("2. Triple DES")
    print("3. RSA")
    print("4. ECC")
    user_choice = input("Enter the number of the decryption algorithm you wish to use: ")
    
    #Load the file and key
    file_data, file_name = load_file()
    key = load_key()
    
    if user_choice == "1":
        decrypt_aes(file_data, file_name, key)
    elif user_choice == "2":
        decrypt_tripledes(file_data, file_name, key)
    elif user_choice == "3":
        decrypt_rsa()
    elif user_choice == "4":
        decrypt_ecc()
    else:
        print("Invalid input. Please try again.")
    
__main__()
