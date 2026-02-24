Discovery Piscine Python:

Module0:
- Learning how to create a folder inside the terminal.
- Learn how to use the print() function to display text to the terminal.
- Learn she bang for execution rights using #!/usr/bin/env at the top of file script.
- Change modification to use executable she bang. 
- Change in terminal using chmod +x {file.name} or can use chmod {binary math} {file.name}.

Module1:


Module2:
- Dealing with conditions. 
- if, elif, else.

Module3:
- How to loop through a condition starting from a number that the user has given, to a specific number. 
- Using while loops. {while number <= 25:}
- How to use a multiplication table:
## print() vs print(f)
> print()
- print() = simple funciton to display values.
- print() = requires string concatenation or .forat() fir variable insertion.
> print(f)
- print(f) = concide wat ot embed vatiables and expressions.
- Uses curly braces inside a string prefixed with f to evaluate expressions.
- print(f) = can use math inside a formatted string literal.
- used print(i, "x", number, "=", number * i) to get a multiplication table inside a loop form 0 - 9.
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
- To solve this i did print(f"Table of {i}:")
- This allows me to write variables within a string?
- The function range() allows me to get the range from one number to the next, e.g. range(0, 11) counts from 0 - 10.
