#!/bin/python3
import sys

arr = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
RES = "".join(chr(x) for x in arr)

F_PATH = "flag.txt"

try:
	with open(F_PATH, "w", encoding='utf-8') as f:
		f.write(RES)
except FileNotFoundError:
		print("Error: flag.txt file not found.")
		sys.exit(1)

print(f"Flag: {RES}\nSolution written to flag.txt")
