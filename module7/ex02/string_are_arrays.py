#!/usr/bin/env python3

import sys

i = 0

if len(sys.argv) != 2:
    print("None")
else:
    z_found = ""
    for i in sys.argv[1]:
        if i == "z":
            z_found += "z"
    if z_found == "":
        print("None")
    else:
        print(z_found)

