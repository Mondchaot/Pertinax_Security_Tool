import hashlib
from Crypto.Cipher import AES
import base64
import os

def sha256(text):
    return hashlib.sha256(text.encode()).hexdigest()

def encrypt_aes(text, key):
    key = key.ljust(32)[:32].encode()
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(text.encode())
    return base64.b64encode(cipher.nonce + tag + ciphertext).decode()

def decrypt_aes(encoded, key):
    data = base64.b64decode(encoded)
    key = key.ljust(32)[:32].encode()
    nonce, tag, ciphertext = data[:16], data[16:32], data[32:]
    cipher = AES.new(key, AES.MODE_EAX, nonce)
    return cipher.decrypt_and_verify(ciphertext, tag).decode()