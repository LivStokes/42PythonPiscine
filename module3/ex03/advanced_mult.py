#!/usr/bin/env python3

i = 0
j = 0

while i in range(0, 11):
    print(f"Table of {i}",  end=": ")
    while j in range(0, 11):
        print(i * j, end=" ")
        j += 1
    print()
    j = 0        
    i += 1
