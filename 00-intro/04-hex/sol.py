#!/bin/python3

import base64

with open("enc", "r", encoding='utf-8') as f:
    enc = f.read().strip()

d_bytes = bytes.fromhex(enc)
flag = base64.b64encode(d_bytes)

print(flag)
