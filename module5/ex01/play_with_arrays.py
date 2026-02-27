#!/usr/bin/env python3

array = [2, 8, 9, 48, 8, 22, -12, 2]
i = 0

print("Original array:", array)

while i < len(array):
    array[i] += 2
    i += 1

print("New array:", array)
