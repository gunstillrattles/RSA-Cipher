import random
import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def generate_key_pair(p, q):
    n = p * q
    phi = (p-1) * (q-1)

    e = random.randrange(1, phi)
    gcd = math.gcd(e, phi)
    while gcd != 1:
        e = random.randrange(1, phi)
        gcd = math.gcd(e, phi)

    d = pow(e, -1, phi)

    return ((e, n), (d, n))
def encrypt(public_key, message):
    e, n = public_key
    cipher = [pow(ord(char), e, n) for char in message]
    return cipher
def decrypt(private_key, cipher):
    d, n = private_key
    message = [chr(pow(char, d, n)) for char in cipher]
    return ''.join(message)
p = 61
q = 53
public_key, private_key = generate_key_pair(p, q)

message = 'Hello, world!'
cipher = encrypt(public_key, message)
decrypted_message = decrypt(private_key, cipher)

print('Original message:', message)
print('Encrypted message:', cipher)
print('Decrypted message:', decrypted_message)
