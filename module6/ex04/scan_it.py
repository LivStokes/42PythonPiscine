#!/usr/bin/env python3

import re
import sys

if len(sys.argv) < 3:
    print("None")
else:
    find = re.findall(sys.argv[1], sys.argv[2])
    print(len(find))
