# migrated from python 2.7
import string

def decode_vigenere(old_decrypted, old_encrypted, new_encrypted):
    decode = lambda x_y: string.uppercase[ord(x_y[1])-ord(x_y[0])]

    key = ''.join(map(decode, list(zip(old_decrypted, old_encrypted))))
    key = key[:[key.startswith(key[1+i:]) for i,_ in enumerate(key)].index(True) + 1] * len(new_encrypted)

    return ''.join(map(decode, list(zip(key, new_encrypted))))