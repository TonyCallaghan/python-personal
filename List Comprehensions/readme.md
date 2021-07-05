# List Comprehension


### The Syntax

`[____ for ____ in ____ ]`
☝ Just remember this

<br>

### Comprehensions vs Looping (eg)
Looping:
`numbers = [1, 2, 3, 4, 5]`

`doubled_numbers = []`

`for num in numbers:`
    `doubled_number = num * 2`
    `doubled_numbers.append(doubled_number)`

`print(doubled_numbers) # [2, 4, 6, 8, 10]`

Using Comprehensions:
`numbers = [1, 2, 3, 4, 5]`

`doubled_numbers = [num * 2 for num in numbers]`

`print(doubled_numbers) # [2, 4, 6, 8, 10]`

cleaner/quicker 🙌
