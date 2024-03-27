import base64, binascii, string

def base64_encode(data):
    data = data.encode()
    return base64.b64encode(data)

def hex_encode(data):
    data = data.encode()
    return binascii.hexlify(data)

def ascii_encode(data):
    return ''.join(str(ord(c)) for c in data)