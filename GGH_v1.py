''' This program is an implementation of the GGH cryptosystem. 
the program outputs the encrypted message and decrypted message, providing that the used private key is orthogonal enough.
'''

from email import message
import numpy as np
import sys
import random

ERROR_VECTOR = np.array([-3.90586627,-45.47095394,-65.20745468])

# This function generates a private and public key

def keyGen(dimension):
    privateKey = []
    print("Searching for a private key")
    ratio = 1
    privateKey = np.identity(dimension)
    print(privateKey)

    print("Searching for a public key")
    while True:
        uniMod = randUniMod(dimension)
        temp = np.matmul(uniMod, privateKey)
        ratio = hadamardRatio(temp, dimension)
        if ratio <= .1:
            publicKey = temp
            break
    print(publicKey)

    return privateKey, publicKey, uniMod

def randUniMod(dimension):
    random_matrix = [[np.random.randint(-10, 10,)
                      for _ in range(dimension)] for _ in range(dimension)]
    upperTri = np.triu(random_matrix, 0)
    lowerTri = [[np.random.randint(-10, 10) if x <
                 y else 0 for x in range(dimension)] for y in range(dimension)]

    #Creating an upper trianglular and lower triangular matrices with diagonals as +1 or -1
    for r in range(len(upperTri)):
    	for c in range(len(upperTri)):
    		if(r == c):
    			if bool(random.getrandbits(1)):
    				upperTri[r][c] = 1
    				lowerTri[r][c] = 1
    			else:
    				upperTri[r][c] = -1
    				lowerTri[r][c] = -1
    uniModular = np.matmul(upperTri, lowerTri)
    return uniModular

	
	#encryption takes as input the message, the public key and the error vector and outputs the encrypted message.'''
def encryption(m, pub_key, e):
	c = np.matmul(m, pub_key) + e
	return c;
	
	#decryption uses Babai's algorithm to decrypt the encrypted message and outputs the original message (if the private key is orthogonal enough).'''
def decryption(c, pri_key, pub_key):
	u = np.matmul(c, np.linalg.inv(pri_key))
	u = np.matmul(np.rint(u), pri_key)
	result = np.matmul(u, np.linalg.inv(pub_key))
	return result;


def check_determinant(matrix):
	det = np.linalg.det(matrix)
	return det;

"""
	This function is used to determine how orthogonal the matrix is 
	close to 1 = orthogonal
	close to 0 = parallel vectors
	the private key should orthogonal enough for a good Basis
"""

# This function returns the Hadamard Ratio of a matrix

def hadamardRatio(matrix, dimension):
    detOfLattice = np.linalg.det(matrix)
    detOfLattice = detOfLattice if detOfLattice > 0 else -detOfLattice
    mult = 1
    for v in matrix:
        mult = mult * np.linalg.norm(v)
    hadRatio = (detOfLattice / mult) ** (1.0/dimension)
    return hadRatio

def perturbation(m, pub_key, c):
	e = c - np.matmul(m, pub_key)
	return e;


public_key  = np.array([[324850,-1625176,2734951],[165782,-829409,1395775],[485054,-2426708,4083804]])
encrypted = np.array([[8930810,-44681748, 75192665]])
private_key = np.array([[58,53,-68],[-110,-112,35],[-10,-119,123]])
decrypted = decryption(encrypted, private_key, public_key)
#print(decrypted)
m =[[714.94261706,3676.99362826,-1717.12356341]]
r = perturbation(m,public_key,encrypted)
#print (r)
det = check_determinant(private_key)
#print(det)
ratio =hadamardRatio(private_key,3)
#print(ratio)
M = np.array([[-49.99999994,-90.99999976,83]])
encrypted = encryption(M, public_key, ERROR_VECTOR)
#print(encrypted)
alice = keyGen(4)
print (keyGen)