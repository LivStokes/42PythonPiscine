#!/usr/bin/env python3

number = int(input("Enter a nuber less than 25\n"))
if number > 25:
    print("Error")
elif number <= 25:
    while number <= 25:
        print("Inside the loop, my variable is", number)
        number += 1
