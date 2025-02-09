# -*- coding: utf-8 -*-
"""
DES,
3DES,
MP5 Hash,
RSA

encrypt the message and output the cipher text.
"""


#DES and 3DES module
import des
#MP5 Hash module
import hashlib
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.hazmat.primitives import hashes

message = "This assignment is the fourth out of six assignments in the course COMP 755."

#this is how to make it a bit string for the encryption
print(message,"\n\n")

#DES
DESkey = des.DesKey(b"eightbit")  #DES key made because key is 8 bits long
#print(DESkey.is_single())
print("After DES Encryption:", end="\n")
print(DESkey.encrypt(message.encode(), padding=True))


#3DES
ThreeDESkey = des.DesKey(b"sixteenbitisused")
#3DES key made because key is 16 bits long
#print(ThreeDESkey.is_triple())
print("\n\nAfter 3DES Encryption:", end="\n")
print(ThreeDESkey.encrypt(message.encode(), padding=True))

#MD5 hash
MDfiveHash = hashlib.md5(message.encode())
print("\n\nMP5 Hash Value:", end="\n")
print(MDfiveHash.digest())

#RSA
RSAPrivateKey = rsa.generate_private_key(public_exponent=65537, key_size=2048)
RSAPublicKey = RSAPrivateKey.public_key()

print("\n\nAfter RSA Encryption with the public key:", end="\n")
print(RSAPublicKey.encrypt(
    message.encode(),
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )))