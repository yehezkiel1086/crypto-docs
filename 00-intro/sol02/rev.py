#!/bin/python3

f_path = "flag.txt"

with open(f_path, "r") as f:
  str_f = f.read()
  arr = list(str_f)
  asc_f = [ord(x) for x in arr]

print(f"String Flag: {str_f}\nReversed (ASCII) flag: {asc_f}")
