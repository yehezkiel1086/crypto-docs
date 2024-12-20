#!/bin/python3

import base64

enc = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
d_bytes = bytes.fromhex(enc)
flag = base64.b64encode(d_bytes)

print(flag)
