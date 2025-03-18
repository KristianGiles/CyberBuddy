from cryptography.fernet import Fernet #pip3 install cryptography

print("        *****        ")
print("      *       *      ")
print("    *  ^     ^  *    ")
print("   *     \\_/     *   ")
print("   *             *   ")
print("    *           *    ")
print("      *       *      ")
print("        *****       ")
print("     \/       \\/      ")
print("     /         \\     ")
print("     \_________/    ")
print("       |     |        ")
print("\nWelcome to CyberBuddy's File Decryption Program!\n")

def load_file():
    # Load the file from the current directory in read-only
    file_name = input("What is the file to load from the current directory: ")
    file_data = open(file_name, "rb").read()
    return file_data, file_name

def load_key():
    # Load the key from the current directory in read-only
    key_name= input("What is the key to load from the current directory: ")
    key = open(key_name, "rb").read()
    return key
    
def decrypt_aes(file_data, file_name):
    # AES decryption using Fernet
    key = load_key()
    f = Fernet(key)
    
    # decrypt data
    decrypted_data = f.decrypt(file_data)
    # write the original file
    with open(file_name, "wb") as file:
        file.write(decrypted_data)
    
    print("File decrypted successfully!")
    
def __main__():
    file_data, file = load_file()
    decrypt_aes(file_data, file)
    
__main__()
