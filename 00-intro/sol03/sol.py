#!/bin/python3

enc = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"
flag = str(bytes.fromhex(enc))

f_path = "flag.txt"

with open(f_path, "w") as f:
	f.write(flag)

print(f"Flag: {flag}\nSolution written in flag.txt")
