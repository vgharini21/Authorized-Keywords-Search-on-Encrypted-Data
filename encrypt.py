from Crypto.Cipher import AES
import base64
import os

KEY = os.urandom(32)  # 256-bit AES key

def encrypt(text):
    cipher = AES.new(KEY, AES.MODE_GCM)
    ciphertext, auth_tag = cipher.encrypt_and_digest(text.encode())
    return base64.b64encode(cipher.nonce + auth_tag + ciphertext).decode()

def decrypt(encrypted_text):
    data = base64.b64decode(encrypted_text)
    nonce, auth_tag, ciphertext = data[:16], data[16:32], data[32:]
    cipher = AES.new(KEY, AES.MODE_GCM, nonce=nonce)
    return cipher.decrypt_and_verify(ciphertext, auth_tag).decode()
