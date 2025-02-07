import hashlib

def hash_keyword(keyword):
    return hashlib.sha256(keyword.encode()).hexdigest()
