// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/4/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
// The algorithm is based on repetitive addition.


// if R0 == 0 END, else R2 = R0
@R0 
D=M   
@END
D;JEQ
@R2
M=D

// if R1 == 0 END, else R1 = R1 - 1
@R1
D=M
@END
D;JEQ
@R1
M=D-1

(LOOP)

    // if R1 == 0 END
    @R1
    D=M
    @END
    D;JEQ

    // R2 = R2 + R0
    @R2
    D=M
    @R0
    D=D+M
    @R2
    M=D

    // R1 = R1 - 1
    @R1
    D=M
    D=D-1
    M=D

    // LOOP
    @LOOP
    0;JMP

(END)
    @8
    0;JMP

