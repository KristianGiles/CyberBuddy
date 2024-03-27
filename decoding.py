import base64, binascii, string

def base64_decode(data):
    data = base64.b64decode(data)
    return data.decode()

def hex_decode(data):
    data = data.encode()
    return binascii.unhexlify(data)

def ascii_decode(data):
    return ''.join(str(chr(c)) for c in data)