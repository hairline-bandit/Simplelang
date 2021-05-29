###Tabs are spaces

To print something, do:

```write "Hello, World"```

To declare a variable, do:

```declare a = 5```

To change a variable after declaration, do:

```a = 10```

To get input, do:

```read "Message: " a```

(The "a" at the end of that is the variable that you are going to put the input)

To turn into an int, do:

```a = integer(a)```

To turn into a string, do:

```a = string(a)```

To turn into a float, do:

```a = decimal(a)```

To turn into a boolean, do:

```a = boolean(a)```

To turn into an array, do:

```a = array(a)```

To get the length of a variable, do:

```a = length(a)```

To get the maximum value of an array, do:

```a = maximum(a)```

To get the minimum value of an array, do:

```a = minimum(a)```

To set something to True, use ```true```

To set something to False, use ```false```

To set something to None, use ```null```

To add 1 to a number, do:

```a++```

To subtract 1 from a number, do:

```a--```

(And use ``` += 2``` to add other values)

To negate a condition, do:

```a = !a```

To use the "pass" keyword, do:

```none```

To use the "continue" keyword, do:

```next```

To use the "break" keyword, do:

```stop```

To use an if statement, do:

```if condition(true)```

To use an else if statement, do:

```elseif condition(true)```

To use an else statement, do:

```else```

To use a for loop, do:

```for i through([1, 2, 3, 4])``` (The "through" keyword means loop *through* an iterable (string or array))

```for i from(1, 10)``` (The "from" keyword means start at the first number, and go up to the second (+= 1 each time) (non-inclusive))

```for i to(10, 1)``` (The "to" keyword means start at the first number, and go down to the second (-= 1 each time) (non-inclusive))

To define a function, do:

```declaref start parameters(x, y)``` (Note that you can leave the space between parentheses for no parameters, but you **must** include ```parameters()```)

To use a while loop, do:

```while condition(true)```

##Built ins

```a = push(5)``` (Appends the value 5 onto the end of the "a" array)

```a = pop(0)``` (Pops the value at the specified index from a the "a" array (you can take away the value to pop from the back))

```a = delete("Value")``` (Removes the specified value from the "a" array)

```a = a split(" ")``` (Makes the "a" variable the array from splitting "a" variable by " ")

```a = a fuse(" ")``` (Makes the "a" variable the string from joining "a" variable by " ")

```a = a index(43)``` (Makes the "a" variable the leftmost index of the value 43 from the "a" array)

```a = a rindex(43)``` (Makes the "a" variable the rightmost index of the value 43 from the "a" array)
