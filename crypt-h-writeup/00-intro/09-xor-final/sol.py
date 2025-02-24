#!/bin/python3

# I've encrypted the flag with my secret key, you'll never be able to guess it.

# Remember the flag format and how it might help you in this challenge!

from pwn import xor

enc = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")

enc_key = xor(enc, "crypto{".encode())

flag = xor(enc, "myXORkey".encode())

print(flag)