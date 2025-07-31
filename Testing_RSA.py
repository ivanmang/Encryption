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
    def egcd_iterative(a, b):
        x0, x1 = 1, 0
        y0, y1 = 0, 1
        while b != 0:
            q, a, b = a // b, b, a % b
            x0, x1 = x1, x0 - q * x1
            y0, y1 = y1, y0 - q * y1
        return a, x0, y0

    gcd, x, _ = egcd_iterative(e, phi)
    if gcd != 1:
        raise Exception("Modular inverse does not exist")
    return x % phi


def generateKeys():
    p = 645
    q = 23
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