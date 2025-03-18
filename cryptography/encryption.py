from cryptography.fernet import Fernet #pip3 install cryptography

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
print("        O||O          ")
print("         ||           ")
print("         \/           ")
print("\nWelcome to CyberBuddy's File Encryption Program!\n")

#Considerations:
#1. What encryption algorithm to use?
#2. What key to use?
#3. What file to encrypt?
#4. Where to save the encrypted file?  
#5. Implementing Padding
#6. Implementing Mode of Operation
#7. Implementing Initialization Vector
#8. Implementing Key Derivation Function
#9. Implementing Key Exchange
    
def load_file():
    # Load the file from the current directory in read-only
    file_name = input("What is the file to load from the current directory: ")
    file_data = open(file_name, "rb").read()
    return file_data, file_name

def encrypt_aes(file_data, file_name): 
    # AES encryption using Fernet
    
    user_input = input("Do you have a key to use? (Y/N): ")
    if user_input in ["Y", "y", "Yes", "yes"]:
        # Load the key from the current directory in read-only
        key_input = input("Enter the key") 
        key = open(key_input, "rb").read() 
        
    elif user_input in ["N", "n", "No", "no"]:
        # Generate a key for AES and save it to a file
        key = Fernet.generate_key()
        with open("aes_key.key", "wb") as key_file:
            key_file.write(key)
    
    # Encrypting the data using a key with Fernet
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(file_data)
    
    # Encrypt the file
    with open(file_name, "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)
    print("File created and written successfully!")

def encrypt_rsa():
    # RSA encryption using
    pass

def __main__():
    file_data, file = load_file()
    # Load the file from the current directory to be used against an encryption algorithm
    
    #If user choice is AES, then encrypt the file with encrypt_aes
    encrypt_aes(file_data, file)
    
__main__()
#run the program