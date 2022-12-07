# Learning Python

# Different ways to create and define variables.
"""
Variable names are case sensitive
cannot start with a number
can only include alphanumeric and underscore
can be used as a short descriptor
longVariableNames_should_be_seperatedBy_Underscore_or_CapitalLettersBetweenEachWord.
"""

AVS = "Colorado Avalanche"
print(AVS)

# You can declare multiple variables in the same line of code.

AVS, YSN, Y22, Y23 = "Colorado Avalanche", "2022-2023", "2022", "2023"
print(AVS)
print(YSN)
print(Y22)
print(Y23)
print()

# You can also pack and unpack lists. The first line is considered the packing phase,
# and is denoted by the use of brackets. This is more memory intensive than tuples.

years = ["2022-2023", "2022", "2023"]
YSN, Y22, Y23 = years
print(YSN)
print(Y22)
print(Y23)
print()

# This is one way to create a tuple. You use parenthesis when packing a tuple.

years = ("2022-2023", "2022", "2023")
YSN, Y22, Y23 = years
print(YSN)
print(Y22)
print(Y23)
print()

# declaring variables globally will work inside nad outside functions unless otherwise
# defined within the function.

x = "awesome"

def myfunc():
    print("Python is " + x)

myfunc()

# Here we redefine the variable x within the function.

def myfunc():
    x = "fantastic"
    print("Python is " + x)

myfunc()

# You can also create a global variable within a function with the global keyword.

print("Python is " + x)

def myfunc():
    global x
    x = "fantastic"

myfunc()

print("Python is " + x)
print()

# Python Data Types
"""
TEXT:     str
NUMERIC:  int, float, complex
SEQUENCE: list, tuple, range
MAPPING:  dict
SET:      set, frozenset
BOOLEAN:  bool
BINARY:   bytes, bytearray, memoryview
NONE:     NoneType
"""

# Each variable has a data type automatically assigned to it when the variable is declared.
# If you can't identify the type, you can get the data type of any object by using the
# "type()" function.
# You can also specify the data type yourself.
# I'll be declaring these variables within a function in order to easily contain them for
# demonstration purposes.

def myfunc():
    a = "Hello World"                          # str
    b = 20                                     # int
    c = 20.5                                   # float
    d = 1j                                     # complex
    e = ["apple", "banana", "cherry"]          # list
    f = ("apple", "banana", "cherry")          # tuple
    g = range(6)                               # range This one is manually declared.
    h = {"name" : "Andrew", "age" : 34}        # dict
    i = {"apple", "banana", "cherry"}          # set
    j = frozenset({"apple", "banana", "cherry"}) # frozenset This one is manually declared.
    k = True                                   # bool
    l = b"Hello"                               # bytes
    m = bytearray(5)                           # bytearray This one is manually declared.
    n = memoryview(bytes(5))                   # memoryview This one is manually declared.
    o = None                                   # NoneType

# See how each data type outputs.

    print(a)
    print(type(a))
    print(b)
    print(type(b))
    print(c)
    print(type(c))
    print(d)
    print(type(d))
    print(e)
    print(type(e))
    print(f)
    print(type(f))
    print(g)
    print(type(g))
    print(h)
    print(type(h))
    print(i)
    print(type(i))
    print(j)
    print(type(j))
    print(k)
    print(type(k))
    print(l)
    print(type(l))
    print(m)
    print(type(m))
    print(n)
    print(type(n))
    print(o)
    print(type(o))

myfunc()
print()

# Converting NUMERIC data types (int, float, complex)

x = 1      # int
y = 2.8    # float
z = 1j     # complex

# int -> float
a = float(x)

# float -> int
b = int(y)

# int -> complex
c = complex(x)

print(a)
print(b)
print(c)
print()
print(type(a))
print(type(b))
print(type(c))
print()

# Notice when converting float to int, python always truncates and chops off the decimal,
# effectively rounding 2.8 down to 2. You can round to nearest integer with round function.
b = round(y)
print(b)
print()

# Python has no random function, but it has a built-in module that behaves the same.
# The number will be randomly generated within that range each time script.py is run.

import random
print(random.randrange(1, 10))
print()