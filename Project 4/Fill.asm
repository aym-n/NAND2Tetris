// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/4/Fill.asm

// Runs an infinite loop that listens to the keyboard input. 
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, 
// the screen should be cleared.

(RESET)
    @SCREEN
    D=A
    @ADDR
    M=D

(LOOP)
    @KBD
    D=M

    @FILL
    D;JNE

    @CLEAR
    0;JMP

(FILL)
    @ADDR
    A=M
    M=-1
    @NEXT
    0;JMP

(CLEAR)
    @ADDR
    A=M
    M=0

(NEXT)
    @ADDR
    D=M+1
    @KBD
    D=A-D

    @RESET
    D;JLE

    @ADDR
    M=M+1

    @LOOP
    0;JMP