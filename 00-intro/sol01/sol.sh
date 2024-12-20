#!/bin/bash

FILE="great_snakes_35381fca29d68d8f3f25c9fa0a9026fb.py"

if [ ! -f "$FILE" ]; then
  wget https://cryptohack.org/static/challenges/great_snakes_35381fca29d68d8f3f25c9fa0a9026fb.py
fi

python3 great_snakes_35381fca29d68d8f3f25c9fa0a9026fb.py | grep -oE "crypto{.*}" > flag.txt

echo -n "Flag: "
cat flag.txt
echo "Solution written to flag.txt"
