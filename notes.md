# Discovery Piscine Python:

## Module0:
- Learning how to create a folder inside the terminal.
- Learn how to use the print() function to display text to the terminal.
- Learn she bang for execution rights using #!/usr/bin/env at the top of file script.
- Change modification to use executable she bang. 
- Change in terminal using chmod +x {file.name} or can use chmod {binary math} {file.name}.

## Module1:


## Module2:
- Dealing with conditions. 
- if, elif, else.

## Module3:
- How to loop through a condition starting from a number that the user has given, to a specific number. 
- Using while loops. {while number <= 25:}
- How to use a multiplication table:
print() vs print(f)
- print()
	- simple funciton to display values.
	- requires string concatenation or .forat() fir variable insertion.
- print(f)
	- Concider what it embed variables and expressions.
	- Uses curly braces inside a string prefixed with f to evaluate expressions.
	- Can use math inside a formatted string literal.
- Used print(i, "x", number, "=", number * i) to get a multiplication table inside a loop form 0 - 9.
- Use break inside a function which immediaty terminates the innermost loop and transfers control to the next statement after the loop.
- break() only breaks the inside loop. Not the outer loops. So if im in a while loop and i have an if statement and i want to break if a condtion is true, then i should not use {while, if, break}. Do something else.
- How i fixed this was writing:
```
#!/usr/bin/env python3

input("What you gotta say? : ")

while True:
    user_input = input("I got that! Anything else? : ")
    if user_input == "STOP":
        break
```
- How to remove spaces in print() funciton. When using a comma, it autoatically gives a space between variables.
- To solve this I did print(f"Table of {i}:")
- This allows me to write variables within a string?
- The function range() allows me to get the range from one number to the next, e.g. range(0, 11) counts from 0 - 10.

## Module 4
- Type checking for numbers. e.g. float,integer, decimal.
- Need to do type checking. Can do this with isinstance() or isdigit().
- isdigit() returns true is all characters in a string are digirs and false if othersie. Onlt works for strings bytes and bytearray objects
- isinstance() checks if an object is an instance of a specified class or type. It works by data type checking includeinf integers, floats, lists and custom classes.
- I never used the function. Instead I created a seperate variable and set it as an integer. Then I asked it if number == checker then it is an int, or visa versa.
- Converting a string characters to its opposing case. 
- lower() returns a string in lowercase.
- upper() returns a string in uppercase.
- swapcase() returns a string with lowercase swapped to uppercase and uppercase swapped to lowercase.

## Module 5
- How to define an array?
- Python does not have built-in support for Arrays, but python lists can be used instead.
- array = [1, 2, 3, 4, 5] || array = ["hello", "my", "name", "is"," Olivia"]
- Or I can use list(). This function creates a list of objects.
- To remove fuplicates from an array, use set().
- 

## Module 6
This module is about parameters.
- Utilising sys.argv to print a specific argumnet to the terminal.

## Module 7


## Module 8
