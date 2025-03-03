#!/bin/python3

def gcd(a, b):
  if a == 0:
    return b
  return gcd(b % a, a)

if __name__ == "__main__":
  print(gcd(35, 15))
  print(gcd(35, 10))
  print(gcd(35, 15))