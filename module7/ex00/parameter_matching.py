#!/usr/bin/env python3

import sys

string = input("What was the parameter?: ")

if len(sys.argv) < 2:
    print("None")
elif sys.argv[1] == string:
    print("Good job!")
else:
    print("Nope, sorry")
