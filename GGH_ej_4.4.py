
import numpy as np
import sys


ERROR_VECTOR = np.array([-1, 1, 1, -1])

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


public_key  = np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[44,18,4,49]])
message = np.array([[3,-4,1,3]])
encrypted = encryption(message, public_key, ERROR_VECTOR)
print(encrypted)
private_key = np.array([[2,-3,1,-4],[-2,1,0,4],[-1,3,2,1],[-1,-4,3,-2]])
decrypted = decryption(encrypted, private_key, public_key)
print(decrypted)
