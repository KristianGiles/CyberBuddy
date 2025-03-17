## Authors: Kristian Giles & Caleb Prince
## Start Date: 16/03/2025
## Last Update: 17/03/2025
## Version Number: 0.3

import argparse
import getpass

from cryptography.password_manager import get_creds, try_connect

#Initialising parser
parser = argparse.ArgumentParser(
    prog='CyberBuddy',
    description='A collation of Cyber Security Utilities'
)

#Initialising arguments
parser.add_argument('-p', '--port', help='Starts up the port scanner, scanning on the specified IP Address, if no IP Address is specified it will scan on your local IP Address, the results of this scan are then outputted.')
parser.add_argument('-i', '--ids', help='Starts up the IDS which will monitor network traffic and alert on suspicious behaviour in perpetuity until stopped.')
parser.add_argument('-s', '--sniffer', help='Starts up a packet sniffer which will analyse flowing packets.')
parser.add_argument('-e', '--encryption', help='Requires an encryption algorithm to be specified, currently supported algorithms TBD')
parser.add_argument('-d', '--decryption', help='Requires a key file to be specified')
parser.add_argument('-a', '--hash', help='Requires a hashing algorithm to be specified, currently supported algorithms TBD')
parser.add_argument('-pm', '--password_manager', action="store_true", help='Opens up the CLI to interface with the password manager backend.')
parser.add_argument('-f', '--file', help='Allows a file to be passed in through stdin')
parser.add_argument('-m', '--malware', help='Analyses malware that is passed in through stdin')
parser.add_argument('-hp', '--honeypot', help='Starts up a Honeypot')
parser.add_argument('-v', '--vuln', help='Starts up a vulnerability scanner.')
parser.add_argument('-k', '--keylogger', help='Begin a keylogger.')
parser.add_argument('-pst', '--strength', help='Allows a password to be passed in and will give it a scoring')

#Creating args Namespace object
args = parser.parse_args()

if args.password_manager == True:
    username, password = get_creds()
    connection = try_connect(username, password)