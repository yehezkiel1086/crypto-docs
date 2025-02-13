#!/bin/python3
import sys

try:
    with open('enc.txt', 'r', encoding='utf-8') as f:
        enc = f.read().strip()  # Remove any extra whitespace or newlines

    try:
        flag = bytes.fromhex(enc).decode('utf-8')
    except UnicodeDecodeError:
        print("Error: The decoded bytes cannot be converted to a UTF-8 string.")
        exit(1)
    except ValueError:
        print("Error: The content of enc.txt is not a valid hex string.")
        exit(1)

    F_PATH = "flag.txt"

    with open(F_PATH, "w", encoding="utf-8") as f:
        f.write(flag)

    print(f"Flag: {flag}\nSolution written in flag.txt")

except FileNotFoundError:
    print("Error: enc.txt file not found.")
    sys.exit(1)