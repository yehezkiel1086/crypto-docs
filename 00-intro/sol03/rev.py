#!/bin/python3
import sys

try:
    with open("flag.txt", "r", encoding='utf-8') as f:
        str_f = f.read().encode('utf-8')

    hex_f = str_f.hex()

    print(hex_f)

except FileNotFoundError:
    print("Error: flag.txt file not found.")
    sys.exit(1)
except UnicodeEncodeError:
    print("Error: The content of flag.txt cannot be encoded to UTF-8.")
    sys.exit(1)