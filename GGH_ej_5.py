''' This program is an implementation of the GGH cryptosystem. 
the program outputs the encrypted message and decrypted message, providing that the used private key is orthogonal enough.
'''

from email import message
import numpy as np
import sys
ERROR_VECTOR = np.array([-3.90586627,-45.47095394,-65.20745468])


def input_handler(filename):
	try:
		with open(filename, 'r') as infile:
			n = sum((1 for line in infile)) #counts lines in infile. This is the expected dimension of the matrix.
			matrix = np.empty([n, n])
			i = 0
			infile.seek(0)
			for line in infile:
				matrix[i] = [int(x) for x in line.split()]
				i = i + 1
	except Exception as e:
		print(e)
		sys.exit(0)
	return matrix, n

	'''generate_public_key takes as input the private key as a matrix and its dimension. 
	Then it multiplies the private key with 5 random unimodular matrices from the right hand side thus creating the public key and outputs it'''
def generate_public_key(n, pri_key):
	k = 0
	matrix = np.identity(n)
	while k < 5:
		A = np.random.randint(-5, 5, size=(n, n))
		if np.linalg.det(A) == 1:
			matrix = np.matmul(matrix, A)
			k = k + 1
	pub_key = np.matmul(matrix, pri_key)
	return pub_key;
	
	'''encryption takes as input the message, the public key and the error vector and outputs the encrypted message.'''
def encryption(m, pub_key, e):
	c = np.matmul(m, pub_key) + e
	return c;
	
	'''decryption uses Babai's algorithm to decrypt the encrypted message and outputs the original message (if the private key is orthogonal enough).'''
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
#message = np.array([[3,-4,1,3]])
#encrypted = encryption(message, public_key, ERROR_VECTOR)
encrypted = np.array([[8930810,-44681748, 75192665]])
#print(encrypted)
private_key = np.array([[58,53,-68],[-110,-112,35],[-10,-119,123]])
decrypted = decryption(encrypted, private_key, public_key)
print(decrypted)
#m = decryption(encrypted, private_key, public_key)
m =[[714.94261706,3676.99362826,-1717.12356341]]
r = perturbation(m,public_key,encrypted)
print (r)
det = check_determinant(private_key)
#det = np.linalg.det(private_key)
print(det)
#public_key = generate_public_key(3, private_key)
#print (public_key)
#privateB=np.random.random_integers(-10,10,size=(3,3))
privateB=np.array([[-97, 19, 19],[-36, 30, 86,],[-184,-64,78]])
ratio =hadamardRatio(private_key,3)
print(ratio)
m = np.array([[-49.99999994,-90.99999976,83]])
encrypted = encryption(m, public_key, ERROR_VECTOR)
#det = np.linal+.det(private_key)
print(encrypted)
#m =[[-49.99999994 -90.99999976  83.        ]]
# r = [[ -3.90586627 -45.47095394 -65.20745468]]
# d = -672858.0
# ratio = 0.6169653190266731
