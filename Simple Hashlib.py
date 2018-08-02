import hashlib

def checkio(hashed_string, algorithm):
    hash = hashlib.new(algorithm)
    hash.update(hashed_string.encode('utf-8'))
    return hash.hexdigest()