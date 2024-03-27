def generate_format_padding(message):
    print('%'*50)
    print(message)
    print('%'*50)

def kill(param, data):
    if param and data:
        return True
    else:
        print("Error! Missing Parameters!")

def print_menu():
    print("1. Password Generator.")
    print("2. Password Tester.")
    print("3. Keylogger Generator.")
    print("4. Encryption")
    print("5. Decryption")
    print("6. Steganography")
    print("7. Packet Sniffer")
    print("8. Hashing")
    print("9. Encoding")
    print("10. Decoding")
    print("11. VirusTotal Check")

def arg_parse_lower(argument):
    try:
        return argument.lower()
    except Exception as e:
        print("Error!")
        quit()