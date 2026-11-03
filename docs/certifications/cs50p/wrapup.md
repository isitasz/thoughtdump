# quick wrap up prior to this note existing

## functions, variables

in python, you dont need to declare variables

input and print are the frequent ones for now.

you can print a string by just using `print(name)` here. so much easier

`print` has a implicit `end='\n'` argument. you can change it by expliciting said argument and putting whatever you want there
there's also `sep=", ")` to separate itens if you're printing a list or smth

use `\"` if you need quotations in a string and is too lazy to change the function ones for single ones.

put an `f` at the start of a string if you want to use variables with `{}` inside of her. example:

```python
smth = "example"
print(f"this is a {smth}")
```

btw you can multiply prints. yeah.

### more in strings

use .method to apply that method to a string
you can stack multiple methods

`strip()` to remove spaces on both sides of str
`title()` title cases the words
`lower()` makes it all lower case

official str documentation:
https://docs.python.org/3/builtins/stdtypes.html#str

### integers and float

the operators are pretty similar to c except you dont have `i++`

use float() or int() to convert

`round(n,[digit])`is self explanatory

you can also use that f thingy from str `print(f"{z:.2f}")`

official documentations:
https://docs.python.org/3/builtins/functions.html#int
https://docs.python.org/3/builtins/functions.html#float

### def

this is what you use to create your own functions.
an example i like, idk why

```python
def hello(to):
    print("hello,", to)

name = input("What's your name? ")
hello(name)
```

`return` can pass manyyyyyyy values. numbers, lists, tumbles, dictionaries... many many stuff.

---

## conditionals

not much to say. just probably the most pythonic part of python

`match` can be used to improve readbility. example:

from:
```python
  name = input("What's your name? ")

  if name == "Harry" or name == "Hermione" or name == "Ron": 
      print("Gryffindor")
  elif name == "Draco":
      print("Slytherin")
  else:
      print("Who?")
```

to:
```python
  name = input("What's your name? ")

  match name: 
      case "Harry" | "Hermione" | "Ron":
          print("Gryffindor")
      case "Draco":
          print("Slytherin")
      case _:
          print("Who?")
```

yes you can use both symbols and just plain english. python moment

official documentation:
https://docs.python.org/3/tutorial/controlflow.html

---

## loops

for in python is pretty weird. it does all the job for you.

like if you want to run 3 times just do `for i in range(3)`. the control variable is created and manipulated automatically.

you can also provide a list such as `for i in [0,1,2]` to be traversed if u want to

you can use `_` in place of `i`. and any variable that serves no purpose other than loop iteration

`break` out of the loop!
`continue` next iteration

if you have any kind of data structure (more about that soon) you can use this formatting:
`for thing in structure`

it will instantly know to follow the list.

    str are included in data structures in this case (cuz its an char list lowkey)

---

## data structures

### lists

various values.

you can make a list and access it like an C array.
```python
example = ["one", "two", "three"]

print(example[0])
# one
print(example[1])
# two
print(example[2])
# three
```

use `len` to see how many items the list contains.

official documentation:
https://docs.python.org/3/builtins/functions.html#len
https://docs.python.org/3/tutorial/datastructures.html#more-on-lists

### dictionaries

basically a list but you can assign value to each item and access it. 
its basically keys with a value.

```python
students = {
    "Hermione": "Gryffindor",
}
print(students["Hermione"])
# Gryffindor
```

    you can make a list of multiple dictionaries!!

official documentation:
https://docs.python.org/3/tutorial/datastructures.html#dictionaries

---


