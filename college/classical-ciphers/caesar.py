#!/bin/python3

def caesar_enc(plain, key):
  enc = ''
  for x in plain:
    char = x
    if char.isupper():
        enc += chr((ord(char) + key - ord('A')) % 26 + ord('A'))
    elif char.islower():
        enc += chr((ord(char) + key - ord('a')) % 26 + ord('a'))
    else:
       enc += char
  return enc

def caesar_dec(enc, key):
  dec = ''
  for x in enc:
    char = x
    if char.isupper():
        dec += chr((ord(char) - key - ord('A')) % 26 + ord('A'))
    elif char.islower():
        dec += chr((ord(char) - key - ord('a')) % 26 + ord('a'))
    else:
       dec += char
  return dec

if __name__ == "__main__":
  option = int(input("Pilih 1 untuk enkrip, 2 untuk dekrip: "))

  if option == 1:
    plain = input("Masukkan plaintext: ")
    key = input("Masukkan key: ")
    enc = caesar_enc(plain, int(key))
    print("Hasil enc: " + enc)
  elif option == 2:
    enc = input("Masukkan enc: ")
    key = input("Masukkan key: ")
    dec = caesar_dec(enc, int(key))
    print("Hasil dec: " + dec)
  else:
    print("Pilihan tidak valid")