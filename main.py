## Project Name: CyberBuddy
## Start Date: 11-05-2023
## Last Edit Date: 24-02-2024
## Author: Kristian Giles
## Description: A large collection of cyber security related functionalities all rolled into one program.
## Version: 1.3

import argparse

from modules.helper_functions import generate_format_padding, kill, arg_parse_lower
from modules.password_generator import primary_password_generator
from modules.password_tester import *
from modules.encoding import base64_encode, hex_encode, ascii_encode
from modules.decoding import base64_decode, hex_decode, ascii_decode
from modules.encryption import *
from modules.decryption import *
from modules.hashing import *
from modules.keylogger import *
from modules.packet_sniffer import *
from modules.steganography import *
from modules.virus_total import *

parser = argparse.ArgumentParser(prog="CyberBuddy", description="A large collection of cyber security related functionalities all rolled into one program.")

parser.add_argument('-g', '--password_generator', action='store_true', help='Generate A Strong Password.\n')
parser.add_argument('-t', '--password_tester', action='store_true')
parser.add_argument('-e', '--encode', help='Pass the encoding type you wish to use(Currently supports Base64, Hex and ASCII)')
parser.add_argument('-n', '--decode')
parser.add_argument('-c', '--encrypt')
parser.add_argument('-o', '--decrypt')
parser.add_argument('-y', '--hashing')
parser.add_argument('-k', '--keylogger')
parser.add_argument('-p', '--packet_sniffer')
parser.add_argument('-s', '--steganography')
parser.add_argument('-v', '--virustotal')
parser.add_argument('-d', '--data')

args = parser.parse_args()

password_gen = args.password_generator
password_test = args.password_tester
encode = args.encode
decode = args.decode
encrypt = args.encrypt
decrypt = args.decrypt
hashing = args.hashing
keylogger = args.keylogger
packet_sniffer = args.packet_sniffer
steganography = args.steganography
virustotal = args.virustotal
data = args.data

if password_gen:
    password = primary_password_generator()
    generate_format_padding(f'Your New Password Is: {password}')

if encode:
    encode = arg_parse_lower(encode)
    kill(encode, data)
    if encode == 'base64':
        encoded_data = base64_encode(data)
        generate_format_padding(f'Encoded Data: {encoded_data}')
    elif encode == 'hex':
        encoded_data = hex_encode(data)
        generate_format_padding(f'Encoded Data: {encoded_data}')
    elif encode == 'ascii':
        encoded_data = ascii_encode(data)
        generate_format_padding(f'Encoded Data: {encoded_data}')

if decode:
    kill(decode, data)
    decode = arg_parse_lower(decode)
    if decode == 'base64':
        decoded_data = base64_decode(data)
        generate_format_padding(f'Decoded Data: {decoded_data}')
    elif decode == 'hex':
        decoded_data = hex_decode(data)
        generate_format_padding(f'Decoded Data: {decoded_data}')
    elif decode == 'ascii':
        decoded_data = ascii_decode(data)
        generate_format_padding(f'Decoded Data: {decoded_data}')

if hashing:
    kill(hashing, data)
    hashing = arg_parse_lower(hashing)
    if hashing == 'md5':
        hashed_data = md5(data)
        generate_format_padding(f'Hashed Data: {hashed_data}')
