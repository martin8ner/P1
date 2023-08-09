#!/usr/bin/python3
from sys import argv
from os import system 

if len(argv)>1: 
    if argv[1]=="-c" or argv[1]=="--clean":
        system("rm *.pdf")
else:
    system("pdftoppm BesselVerfahren.pdf BesselVerfahren -png -cropbox")
    system("mv BesselVerfahren-1.png BesselVerfahren.png")

