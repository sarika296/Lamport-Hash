#Implemented in python

# Simple Python implementation of Lamport signature scheme

import hashlib
import math
import secrets
import sys

CHAR_ENC = 'utf-8'
BYTE_ORDER = sys.byteorder
Alice = 0
Bob = 1

# Generate a keypair for a one-time signature
def keygen():
    Alice = [[0 for x in range(256)] for y in range(2)]
    Bob = [[0 for x in range(256)] for y in range(2)] 
    for i in range(0,256):
        #secret key
        Alice[0][i] = secrets.token_bytes(32)
        Alice[1][i] = secrets.token_bytes(32)
        #public key
        Bob[0][i] = hashlib.sha256(Alice[0][i]).digest()
        Bob[1][i] = hashlib.sha256(Alice[1][i]).digest()

    keypair = [Alice,Bob]
    return keypair

# Sign messages using Lamport one-time signatures
def sign(m, Alice):
    sig = [0 for x in range(256)]
    h = int.from_bytes(hashlib.sha256(m.encode(CHAR_ENC)).digest(), BYTE_ORDER)
    for i in range(0,256):
        b = h >> i & 1
        sig[i] = Alice[b][i]

    return sig

# Verify Lamport message signatures
def verify(m, sig, Bob):
    h = int.from_bytes(hashlib.sha256(m.encode(CHAR_ENC)).digest(), BYTE_ORDER)
    for i in range(0,256):
        b = h >> i & 1
        check = hashlib.sha256(sig[i]).digest()
        if Bob[b][i] != check:
            return False

    return True

keypair = keygen()
message = "Lamport signatures !"
sig = sign(message, keypair[Alice])
print(verify(message, sig, keypair[Bob]))
