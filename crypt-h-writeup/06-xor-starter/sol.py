#!/bin/python3

from pwn import xor

enc = "label"
xor_enc = "".join([chr(ord(xor(x, 13))) for x in enc])
print("crypto{" + xor_enc + "}")