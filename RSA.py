import math


# Find the modular inverse of e modulo phi(n)
def calculate_d(e, phi_n):
    for d in range(1, phi_n):
        if (e * d) % phi_n == 1:
            return d
    return None


# RSA Encryption
def encrypt(message, e, n):
    encrypted_message = []

    for char in message:
        encrypted_value = pow(ord(char), e, n)
        encrypted_message.append(encrypted_value)

    return encrypted_message


# RSA Decryption
def decrypt(encrypted_message, d, n):
    decrypted_message = ""

    for value in encrypted_message:
        decrypted_message += chr(pow(value, d, n))

    return decrypted_message


# Main Program
if __name__ == "__main__":

    # Step 1: Choose two prime numbers
    p = 17
    q = 19

    # Step 2: Calculate n
    n = p * q

    # Step 3: Calculate Euler's Totient
    phi_n = (p - 1) * (q - 1)

    # Step 4: Choose public exponent e
    e = 5

    # e and phi(n) must be coprime
    if math.gcd(e, phi_n) != 1:
        print("Invalid value of e")
    else:

        # Step 5: Calculate private key d
        d = calculate_d(e, phi_n)

        # Original message
        message = "HELLO"

        # Encryption
        encrypted_message = encrypt(message, e, n)
        print("Encrypted message:", encrypted_message)

        # Decryption
        decrypted_message = decrypt(encrypted_message, d, n)
        print("Decrypted message:", decrypted_message)