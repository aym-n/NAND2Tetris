import sys

if len(sys.argv) <= 1:
    print("USAGE: assembler.py [INPUT FILE]")
    exit(1)

filePath = sys.argv[1] + ".asm"
outFilePath = sys.argv[1] + ".hack"
SYMBOL_TABLE = {}

# Populate SYMBOL_TABLE
with open("symbols.txt", "r") as symbols:
    for line in symbols:
        label , address = tuple(line.rstrip("\n").split(" "))
        SYMBOL_TABLE[label] = address

COMP_TABLE = {
    "0": "0101010",
    "1": "0111111",
    "-1": "0111010",
    "D": "0001100",
    "A": "0110000",
    "!D": "0001101",
    "!A": "0110001",
    "-D": "0001111",
    "-A": "0110011",
    "D+1": "0011111",
    "A+1": "0110111",
    "D-1": "0001110",
    "A-1": "0110010",
    "D+A": "0000010",
    "D-A": "0010011",
    "A-D": "0000111",
    "D&A": "0000000",
    "D|A": "0010101",
    "M": "1110000",
    "!M": "1110001",
    "-M": "1110011",
    "M+1": "1110111",
    "M-1": "1110010",
    "D+M": "1000010",
    "D-M": "1010011",
    "M-D": "1000111",
    "D&M": "1000000",
    "D|M": "1010101"
    }

DEST_TABLE = {
    "null": "000",
    "M": "001",
    "D": "010",
    "A": "100",
    "MD": "011",
    "AM": "101",
    "AD": "110",
    "AMD": "111"
    }


JMP_TABLE = {
    "null": "000",
    "JGT": "001",
    "JEQ": "010",
    "JGE": "011",
    "JLT": "100",
    "JNE": "101",
    "JLE": "110",
    "JMP": "111"
    }



symbols.close()
variable_pos = 16

# Read .asm file
lines = []
line_number = 0

with open(filePath) as file:
    for line in file:
        # Remove Comments
        line = line.split("//")
        line = line[0].strip()

        if line == "":
            continue

        # Add Labels to SYMBOL_TABLE
        if line.startswith("("):
            label = line[1:-1].strip()
            SYMBOL_TABLE[label] = line_number
        else:
            line_number += 1
            lines.append(line)
    file.close()

def translateA(line):
    global variable_pos
    # Get Value of Label
    label = line[1:]
    if not label.isdigit():
        if label not in SYMBOL_TABLE:
            SYMBOL_TABLE[label] = variable_pos
            variable_pos += 1
        value = SYMBOL_TABLE[label]
    else:
        value = label

    return bin(int(value))[2:].zfill(16)


def translateC(line):
    # Normalise C instruction int A=B;C
    if not "=" in line:
        line = "null=" + line

    if not ";" in line:
        line = line + ";null"

    instruction = line.split("=")
    destCode = DEST_TABLE.get(instruction[0])
    instruction = instruction[1].split(";")
    compCode = COMP_TABLE.get(instruction[0])
    jmpCode = JMP_TABLE.get(instruction[1])

    # Return 111-CCCCCCC-DDD-JJJ
    return '111' + compCode + destCode + jmpCode

def translate(line):
    if line[0] == '@':
        return translateA(line)
    return translateC(line)

outputFile = open(outFilePath, "w")

for line in lines:
    outline = translate(line)
    outputFile.write(outline + "\n")


    
