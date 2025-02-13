#!/bin/python3
import sys

F_PATH = "flag.txt"

try:
    with open(F_PATH, "r", encoding="utf-8") as f:
        str_f = f.read()
        arr = list(str_f)
        asc_f = [ord(x) for x in arr]
except FileNotFoundError:
    print("Error: flag.txt file not found.")
    sys.exit(1)

print(f"String Flag: {str_f}\nReversed (ASCII) flag: {asc_f}")
