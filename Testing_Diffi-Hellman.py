
def power(a, b, p):
    if b == 1:
        return a
    else:
        return pow(a, b) % p

def encrypt_message(message, secret):
    encrypted_message = ""
    key = secret
    for c in message:
        encrypted_message += chr(ord(c) + key)
    return encrypted_message

def decrypt_message(message, secret):
    decrypted_message = ""
    key = secret
    for c in message:
        decrypted_message += chr(ord(c) - key)
    return decrypted_message


def main():

    P = 23
    print("The value of P:", P)


    G = 9
    print("The value of G:", G)


    a = 4
    print("The private key a for Alice:", a)


    x = power(G, a, P)


    b = 3
    print("The private key b for Bob:", b)


    y = power(G, b, P)


    ka = power(y, a, P)
    kb = power(x, b, P)

    print("Secret key for Alice is:", ka)
    print("Secret key for Bob is:", kb)

    C = encrypt_message("hello", ka)
    print("encrypted: ", C)

    D = decrypt_message(C, kb)
    print("decrypted: ", D)



if __name__ == "__main__":
    main()