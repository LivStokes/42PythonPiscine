#!/usr/bin/env python3

age = int(input("Please tell me your age: "))
year = list(range(10, 31, 10))

print(f"You are currently {age} years old.")

i = 0

while i < 40:
    print(f"In {i} years, you'll be {i + age} years old.")
    i += 10
