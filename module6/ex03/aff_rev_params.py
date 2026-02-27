#!/usr/bin/env python3

import sys

arg_c = len(sys.argv)
i = arg_c - 1

if arg_c < 3:
    print("None")
else:
    while i > 0:
        print(sys.argv[i])
        i -= 1
