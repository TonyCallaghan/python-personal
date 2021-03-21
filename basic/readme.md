# Basic Python Notes

Notes created from Udemy python course. 

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
