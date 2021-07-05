# List Comprehension


### The Syntax

`[____ for ____ in ____ ]`

☝ Just remember this

<br>

### Comprehensions vs Looping (eg)
##### Looping:

`numbers = [1, 2, 3, 4, 5]`

`doubled_numbers = []`

`for num in numbers:`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `doubled_number = num * 2`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`doubled_numbers.append(doubled_number)`

`print(doubled_numbers) # [2, 4, 6, 8, 10]`


##### Using Comprehensions:

`numbers = [1, 2, 3, 4, 5]`

`doubled_numbers = [num * 2 for num in numbers]`

`print(doubled_numbers) # [2, 4, 6, 8, 10]`

cleaner/quicker 🙌

<br>

### Examples:

1. `[num*10 for num in range(1,6)] # [10, 20, 30, 40, 50]`

2. `[bool(val) for val in [0, [], '']] # [False, False, False]`

3. `numbers = [1, 2, 3, 4, 5]`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `string_list = [str(num) for num in numbers]`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `print(string_list) # ['1', '2', '3', '4', '5']`

<br>

### LC with conditional Logic


You can have if/else statments with list comprehensions 🙌


1. `numbers = [1, 2, 3, 4, 5, 6]`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `evens = [num for num in numbers if num % 2 == 0]`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `odds = [num for num in numbers if num % 2 != 0]`


2. `[num*2 if num % 2 == 0 else num/2 for num in numbers] `

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `# [0.5, 4, 1.5, 8, 2.5, 12]`


3. `with_vowels = "This is so much fun!" `

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `''.join(char for char in with_vowels if char not in "aeiou")`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `# "Ths s s mch fn!" `
