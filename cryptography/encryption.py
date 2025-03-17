#Importing the Fernet module from the cryptography library
from cryptography import Fernet

#Fernet is a symmetric encryption algorithm that is used for secure messaging
#LIMITATIONS: files must fit in available memory to be able to be encrypted/decrypted

print("       *****       ")
print("     *       *     ")
print("    *  O   O  *    ")
print("    *    ∆    *    ")
print("    *  \\___/  *    ")
print("     *       *     ")
print("       *****       ")
print("Welcome to CyberBuddy's File Encryption Program!\n")

#User will upload file to be encrypred or run the program against a file to encrypt
    #Option 1. print("Upload the file you wish to encrypt: ")
    #Option 2. CyberBuddy.py examplefile.txt

print("File uploaded successfully!\n")
print("Would you like to create a new encryption key or use an existing one?")
encryption_key_selection = input(print("Would you like to create a new encryption key or use an existing one?\nEnter 1 to create a new key or 2 to use an existing key"))
#User chooses to create a new encryption key or use an existing one
if encryption_key_selection == 1 or "Yes" or "yes" or "YES" or "y" or "Y" or "1" or "True" or "true":
    #Generating a key
    key = Fernet.generate_key()
    print(key)
elif encryption_key_selection == 2 or "No" or "no" or "NO" or "n" or "N" or "nO" or "2" or "False" or "false":
    #User inputs the key
    key = input(print("Enter the key: "))
    
    #
    
    
#Prompt the user to download the file
download_key_selection = input(print("Would you like to download the key to a file?\n Enter 1 or yes to download the key, or 2 or no to not download the key"))
#User chooses if they want to download the key to a file
if download_key_selection == 1 or "Yes" or "yes" or "YES" or "y" or "Y" or "1" or "True" or "true":
    #Prompt the user to name the file and downloads in the current directory, if the user enters nothing, it names the fle encryption_key.txt
    input("What would you like to name the key file? ")
    if input == "":
        with open("encryption_key.txt", "w") as file:
            file.write("Encryption_Key")
    else: 
        with open(input, "w") as file:
            file.write("Encryption_Key")
elif download_key_selection == 2 or "No" or "no" or "NO" or "n" or "N" or "nO" or "2" or "False" or "false":
    print("Key not downloaded")
else:
    print("Enter the correct answer or else.")

