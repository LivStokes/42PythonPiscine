#!/usr/bin/env python3

import sys

i = 1

if len(sys.argv) < 2:
    print("None")
while i < len(sys.argv):
    if i != len(sys.argv) - 1:
        print(sys.argv[i].lower(), end=" ")
    else:
        print(sys.argv[i].lower())
    i += 1

