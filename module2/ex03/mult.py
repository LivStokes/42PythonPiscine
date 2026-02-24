#!/usr/bin/env python3

first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
result = first_number * second_number

print(first_number, "x", second_number, "=", result, sep=" ")

if result < 0:
    print("The result is negative")
elif result > 0:
    print("The result is positive")
elif result == 0:
    print("The result is postive and negative")
