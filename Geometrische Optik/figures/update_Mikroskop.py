#!/usr/bin/python3
from sys import argv
from os import system 

if len(argv)>1: 
    if argv[1]=="-c" or argv[1]=="--clean":
        system("rm *.pdf")
else:
    system("pdftoppm Mikroskop.pdf Mikroskop -png -cropbox")
    system("mv Mikroskop-1.png Mikroskop.png")

