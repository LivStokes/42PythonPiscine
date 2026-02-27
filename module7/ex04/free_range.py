#!/usr/bin/env python3

import sys

if len(sys.argv) != 3:
    print("None")
else:
    arg1 = int(sys.argv[1])
    arg2 = int(sys.argv[2])
    if arg1 < arg2:
        result = list(range(arg1, arg2 + 1))
        print(result)
    else:
        print("None")
