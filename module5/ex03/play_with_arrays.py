#!/usr/bin/env python3

array = [2, 8, 9, 48, 8, 22, -12, 2]
result = []
i = 0
print(array)

while i < len(array):
    if array[i] > 5:
        result.append(array[i] + 2)
    i += 1
print(set(result))

