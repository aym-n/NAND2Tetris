import sys

if len(sys.argv) <= 1:
    print("USAGE: assembler.py [FILENAME]")
    exit(1)

filePath = sys.argv[1]
SYMBOL_TABLE = {}

with open("symbols.txt", "r+") as symbols:
    for line in symbols:
        label , address = tuple(line.rstrip("\n").split(" "))
        SYMBOL_TABLE[label] = address


