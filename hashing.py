import hashlib, binascii

#md5, sha1, sha256, sha512, ntlm

def md5(word):
    word = word.encode()
    word = hashlib.md5(word)
    return word.hexdigest()


