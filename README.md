# Basic Python Notes

Notes **I** created when learning Python. 

## Numbers, Operators, and Comments
`+` `-` `/` `*` `%`

☝ all work the same as any other language.

`/` will always return float

> 56 / 8 returns 7.0

<br>

### New ones to note..
`**` To the power

> 3**3 returns 27 (int)

`//` divide without remainder

> 56.2 / 8 = 7.0

☝ Rounds down to nearest whole number

<br>

### Comments
`#` Single Line Comment

No such thing as a multi line comment in Python.

<br>

## Naming Conventions
- Most variables should be **snake_case** (underscores between words)

`my_answer = 43`

- Most variablkes should be lowercase with some exceptions:
  1. **CAPITAL_SNAKE_CASE** usually refers to constants `VALUE_OF_PI = 3.14`
  2. **UpperCamelCase** usually refers to a class.

- Variables that start/end with 2 underscores, supposed to be private/left alone
`__Dont_touch__`


<br>


## Data Types in Python
Basically 👇
| Type       | Desc.                                                                          | 
| :--------: |:------------------------------------------------------------------------------:| 
| `bool`     | **Boolean** `True` `False` (Remember cap 1st letter)                           | 
| `int`      | **Integer**  1,2,3                                                             |  
| `str`      | **String** `"Tony"`                                                            |  
| `list`     | Ordered sequence of values of other data types e.g `[1,2,3]` or `["a","b","c"]`| 
| `dict`     | a collection of key values e.g `{"first_name": "John", "last_name": "Doge"}`   | 

<br>

## Python is Dynamically Typed

- Like JS, you can change data types to whatever you want them
- For example:

 1.`i_am_string = "hello world"`


 2.`i_am_string = 73 ` 


 3.`i_am_string = True`
- Python doesn't care (won't return error) 😃

> `type(i_am_string)` would return *bool*.

<br>

## String Escape sequences 
- Work exactly the same as any other language.
> `\n` would give a new line.
> `\\` would give a backslash.
etc..

## String Concatention (Formating)
- Bit differnt with Python(3.6)
- Several ways to format Strings in python to *interpolate* variables.
- For example:

1.`x = 10`


2.`formatted = f"I've told you {x} times, already!"`


3.`print(formatted)`


> I've told you 10 times, already!

<br>

## Converting Data Types
- Changing double to int


1.`dec = 12.345`


2.`integer = int(dec)`


3.`print(integer)`


> 12

- Changing Ints to Strings etc..


1.`my_list = [1,2,3]`


2.`my_new_list = str(my_list)`


3.`print(my_new_list)`


> "[1,2,3]"

<br>

## Condition Logic

- Works the same 🙌
- Just remember instead of `else if()` Python uses `elif` 🤦
- Use `:` instead of `{}` & theres no need for parameters`()` 
- REMEMBER INDENTATION 📢
- Example:


1.`if name == "Tony":`


2.    `Print("Hello Tony!")`


3.`elif name == "guest":`

4.    `Print("Hello Guest!")`

<br>

## Conditional Logic cont.

In your conditional statements:
- `and` is the same as `&&`
- `or` is the same as `||`
- `not` is kinda the same as `!`

<br>

- `is` is **NOT** the same as `==`
- `is` is only true if the variables/lists reference the same item in memory
- Example:


1.`c=b`


2.`b is c` #true

