#!/usr/bin/python3
from sys import argv
from os import system 

if len(argv)>1: 
    if argv[1]=="-c" or argv[1]=="--clean":
        system("rm *.pdf")
else:
    system("pdftoppm Linsengleichung.pdf Linsengleichung -png -cropbox")
    system("mv Linsengleichung-1.png Linsengleichung.png")

