def vigenere_encrypt(plaintext, key):
    use_plaintext = plaintext.upper()
    use_key = key.upper()
    
    ciphertext = ""
    for i in range(len(use_plaintext)):
        ciphertext += chr((ord(use_plaintext[i]) + ord(use_key[i % len(use_key)])) % 26 + ord("A"))
    return ciphertext

def vigenere_decrypt(ciphertext, key):
    use_ciphertext = ciphertext.upper()
    use_key = key.upper()
    
    plaintext = ""
    for i in range(len(use_ciphertext)):
        plaintext += chr((ord(use_ciphertext[i]) - ord(use_key[i % len(use_key)])) % 26 + ord("A"))
    return plaintext

plaintext = "MENCARI"
key = "IUKCSKU"

print(vigenere_encrypt(plaintext, key))