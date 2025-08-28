# Caesar Cipher

# Encryption
def encrypt(original_text, shift_amount):
    temp = list(original_text)
    for i in range(len(temp)):
        temp[i] = chr(ord(temp[i]) + shift_amount)
    
    encrypted_text = ''.join(temp)
    print(encrypted_text)

# Decryption
def decrypt(original_text, shift_amount):
    temp = list(original_text)
    for i in range(len(temp)):
        temp[i] = chr(ord(temp[i]) - shift_amount)
    
    decrypted_text = ''.join(temp)
    print(decrypted_text)


def caesar():
    