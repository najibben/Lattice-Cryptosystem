''' This program is an implementation of the GGH cryptosystem. 
The user inputs the name of the file containing private key on the command line. For example
"python ggh.py input.txt". The input file must contain a square matrix with base vectors of the private key as rows.
Coordinates must be separated by a space. Then the program prompts the user for the integer vector they wish to encrypt.
Then the program outputs the encrypted message and decrypted message, providing that the used private key is orthogonal enough.
NOTE: GGH should NOT be used to encrypt anything as it has been broken. 
This program is just an example of how the cryptosystem works.'''

import numpy as np
import sys
from Babai import *


ERROR_VECTOR = np.array([-1, 1, 1, -1])


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
'''encryption takes as input the message, the public key and the error vector and outputs the encrypted message.'''
def encryption(m, pub_key, e):
	c = np.matmul(m, pub_key) + e
	return c;
	
'''decryption uses Babai's algorithm to decrypt the encrypted message and outputs the original message (if the private key is orthogonal enough).'''
def decryption(c, pri_key, pub_key):
	u = np.matmul(c, np.linalg.inv(pri_key))
	u = np.matmul(np.rint(u), pri_key)
	#unimodular = np.array([[0, -2, 1, 0], [-1, 0, 1, -2], [2, 0, 2, -1], [-1, 1, 3, 1]])
	#m =np.round(np.matmul(u,unimodular)).astype(int)#np.round(np.matmul(BB,unimodular1)).astype(int)
	result = np.matmul(u, np.linalg.inv(pub_key))
	return result;


filename = sys.argv[-1]
private_key, dimension = input_handler(filename)
#public_key = generate_public_key(dimension, private_key)
public_key  = np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[44,18,4,49]])
message = np.empty(dimension)
message = [int(x) for x in input("Input the integer vector you wish to encrypt ").split()]
message = np.array([[3,-4,1,3]])
encrypted = encryption(message, public_key, ERROR_VECTOR)
print(encrypted)
#private_key = np.array([[2,-3,1,-4],[-2,1,0,4],[-1,3,2,1],[-1,-4,3,-2]])
decrypted = decryption(encrypted, private_key, public_key)
print(decrypted)
