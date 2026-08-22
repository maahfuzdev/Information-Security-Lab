def caesar_encrypt(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            ciphertext += chr((ord(char)-shift_base+shift)%26+shift_base)
        else:
            ciphertext += char
    return ciphertext

def caesar_decrypt(ciphertext, shift):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            plaintext += chr((ord(char)-shift_base-shift)%26+shift_base)
        else:
            plaintext += char
    return plaintext

# Example usage
plaintext = input("Enter the plaintext for Caesar Cipher: ")
shift = int(input("Enter the shift value: "))
encrypted = caesar_encrypt(plaintext, shift)
print(f"Encrypted: {encrypted}")
decrypted = caesar_decrypt(encrypted, shift)
print(f"Decrypted: {decrypted}")