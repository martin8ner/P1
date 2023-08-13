#!/usr/bin/python3
from sys import argv
from os import system 

if len(argv)>1: 
    if argv[1]=="-c" or argv[1]=="--clean":
        system("rm *.pdf")
else:
    system("pdftoppm AbbeVerfahren.pdf AbbeVerfahren -png -cropbox")
    system("mv AbbeVerfahren-1.png AbbeVerfahren.png")

