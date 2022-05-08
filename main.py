from GGH import *

# key generation for two subscribers
Alice = GGH(10)
Alice.CryptGenKey()
Bob   = GGH(10)
Bob.CryptGenKey()

# allocation of public keys of subscribers
pub_Alice = Alice.CryptGetUserKey()
pub_Bob   = Bob.CryptGetUserKey()


# Bob encrypts a message for Alice:
m = np.random.randint(-100, 100, pub_Alice.dim)
print(m)
c = pub_Alice.CryptEncrypt(m)
print(c)
# Alice descifra un mensaje de Bob:
M = Alice.CryptDecrypt(c)
print(M)
# validación:
if np.all(M == m):
    print('received')

# Alice cifra un mensaje para Bob:
m = np.random.randint(-100, 100, pub_Bob.dim)
print(m)
c = pub_Bob.CryptEncrypt(m)
print(c)

#Bob descifra un mensaje de Alice :
M = Bob.CryptDecrypt(c)
print(c)
# validación:
if np.all(M == m):
    print('received')
