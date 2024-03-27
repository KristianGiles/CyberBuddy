from modules.decoding import base64_decode, hex_decode, ascii_decode
from modules.encoding import base64_encode, hex_encode, ascii_encode
from modules.hashing import md5
from modules.helper_functions import kill
from modules.password_generator import password_generator_level1, password_generator_level2, password_generator_level3, password_generator_level4, password_generator_level5, primary_password_generator
from modules.virus_total import create_client, kill_client, file_information

def test_base64_decode():
    assert base64_decode("aGVsbG8gd29ybGQK") == "hello world\n"

def test_hex_decode():
    assert hex_decode("68656c6c6f20776f726c64") == b"hello world"

def test_ascii_decode():
    assert ascii_decode("&#104;&#101;&#108;&#108;&#111;&#32;&#119;&#111;&#114;&#108;&#100;") == "hello world"

def test_password_generator():
    assert len(primary_password_generator()) == 24