def power(base, expo, m):
    res = 1
    base = base % m
    while expo > 0:
        if expo & 1:
            res = (res * base) % m
        base = (base * base) % m
        expo = expo // 2
    return res



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


def generateKeys():
    p = 645645
    q = 2345
    n = p * q
    phi = (p - 1) * (q - 1)
    print("n: ", n)
    print("phi: ", phi)

    e = 0
    for e in range(2, phi):
        if gcd(e, phi) == 1:
            break

    print("e:", e)
    d = modInverse_extend(e, phi)

    return e, d, n



def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a



def encrypt(m, e, n):
    return power(m, e, n)



def decrypt(c, d, n):
    return power(c, d, n)



if __name__ == "__main__":

    e, d, n = generateKeys()

    print(f"Public Key (e, n): ({e}, {n})")
    print(f"Private Key (d, n): ({d}, {n})")

    M =  12345
    print(f"Original Message: {M}")

    C = encrypt(M, e, n)
    print(f"Encrypted Message: {C}")

    decrypted = decrypt(C, d, n)
    print(f"Decrypted Message: {decrypted}")