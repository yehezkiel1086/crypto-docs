#!/bin/python3

arr = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
res = "".join(chr(x) for x in arr)

f_path = "flag.txt"

with open(f_path, "w") as f:
	f.write(res)

print(f"Flag: {res}\nSolution written to flag.txt")
