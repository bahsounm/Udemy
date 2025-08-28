# Caesar Cipher
import art 
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


# encrpyt asnd decrypt are the same just the plus or minus use the idea of * by -1

def caesar(original_text, shift_amount, encode_or_decode):
    ans = 1
    if encode_or_decode == "decode":
        ans = -1
    temp = list(original_text)
    for i in range(len(temp)):
        temp[i] = chr(ord(temp[i]) + shift_amount*ans)
    
    text = ''.join(temp)
    print(f"Here is the result: {text}")



print(art.art)
while True:
    decode_or_encode = input("Type 'encode' to encrpty or 'decode' to decrypt:\n")
    original_text = input("Type your message:\n")
    shift_amount = int(input("Type your shift number:\n"))
    caesar(original_text, shift_amount, decode_or_encode)
    nxt_step = input("Type 'yes' if you want to go again. Otherwise type 'no'\n")
    if nxt_step == 'no':
        break
