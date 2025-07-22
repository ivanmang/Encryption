# Python Program for implementation of RSA Algorithm

def power(base, expo, m):
    res = 1
    base = base % m
    while expo > 0:
        if expo & 1:
            res = (res * base) % m
        base = (base * base) % m
        expo = expo // 2
    return res


# Function to find modular inverse of e modulo phi(n)
# Here we are calculating phi(n) using Hit and Trial Method
# but we can optimize it using Extended Euclidean Algorithm
def modInverse(e, phi):
    for d in range(2, phi):
        if (e * d) % phi == 1:
            return d
    return -1

# compute modular inverse using Extended Euclidean Algorithm
def modInverse_extend(e, phi):
    def egcd(a, b):
        if a == 0:
            return b, 0, 1
        gcd, x1, y1 = egcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y

    gcd, x, _ = egcd(e, phi)
    if gcd != 1:
        raise Exception("Modular inverse does not exist")
    return x % phi


# RSA Key Generation
def generateKeys():
    p = 645645
    q = 2345
    n = p * q
    phi = (p - 1) * (q - 1)
    print("phi: ", phi)
    # Choose e, where 1 < e < phi(n) and gcd(e, phi(n)) == 1
    e = 0
    for e in range(2, phi):
        if gcd(e, phi) == 1:
            break

    # Compute d such that e * d ≡ 1 (mod phi(n))
    print("e:", e)
    x2 = time.time()
    d = modInverse_extend(e, phi)
    x3 = time.time()

    print("It took", x1 - x0, "seconds!")
    return e, d, n


# Function to calculate gcd
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# Encrypt message using public key (e, n)
def encrypt(m, e, n):
    return power(m, e, n)


# Decrypt message using private key (d, n)
def decrypt(c, d, n):
    return power(c, d, n)


# Main execution
if __name__ == "__main__":
    start = time.time()
    # Key Generation
    e, d, n = generateKeys()

    print(f"Public Key (e, n): ({e}, {n})")
    print(f"Private Key (d, n): ({d}, {n})")

    # Message
    M =  456
    print(f"Original Message: {M}")

    # Encrypt the message
    C = encrypt(M, e, n)
    print(f"Encrypted Message: {C}")

    # Decrypt the message
    decrypted = decrypt(C, d, n)
    print(f"Decrypted Message: {decrypted}")
    end = time.time()