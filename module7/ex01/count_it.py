#!/usr/bin/env python3

import sys

i = 1

if len(sys.argv) < 2:
    print("None")
else:
    while i < len(sys.argv):
        print(sys.argv[i] + ":",  len(sys.argv[i]))
        i += 1
