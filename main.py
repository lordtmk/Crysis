import os
import sys
from Crypto.Cipher import Salsa20
from Crypto.Hash import SHA256
import base64

KEY = b"\xec\xe7\xa3\x1b\x99`\x1f\x87\x8b\xe6\x08f\x05\x8b\x058\xfbz'\xd0\xbe\x1ak\x05a.\xd9\x84\xd9\xfb\x1a\x9d"

def list_files(directory):
    """
    Lists all files in a directory
    """
    for root, dirs, files in os.walk(directory):
        for file in files:
            print(os.path.join(root, file))
            
def encrypt(file):
    cipher = Salsa20.new(key=KEY)
    
    with open(file, "rb") as f:
        data = f.read()
    
    buf = cipher.nonce + cipher.encrypt(data)
    
    with open(file, "wb") as f:
        f.write(buf)

def decrypt(file):
    
    with open(file, "rb") as f:
        data = f.read()
        
    cipher = Salsa20.new(key=KEY, nonce=data[:8])
    buf = cipher.decrypt(data[8:])
    
    with open(file, "wb") as f:
        f.write(buf)
        
decrypt("test.txt")
    
