#!/usr/bin/env python3

import sys

if len(sys.argv) < 2:
    print("None")
else:
    for i in sys.argv[1:]:
        if i.endswith("ism"):
            continue
        else:
            print(f"{i}ism")
