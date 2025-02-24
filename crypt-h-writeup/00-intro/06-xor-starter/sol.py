#!/bin/python3

enc = "label"

enc_bin = "".join([chr(ord(x) ^ 13) for x in enc])

print("crypto{" + enc_bin + "}")