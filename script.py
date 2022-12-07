# Learning Python
# Make a script to automate display configuration settings on startup.
AVS = "Colorado Avalanche \n    2022-2023\n"
print(AVS)

AVS, YSN, Y22, Y23 = "Colorado Avalanche", "2022-2023", "2022", "2023"
print(AVS)
print(YSN)
print(Y22)
print(Y23)

years = ("2022-2023", "2022", "2023")
YSN, Y22, Y23 = years
print(YSN)
print(Y22)
print(Y23)

x = "awesome"

def myfunc():
    print("Python is " + x)

myfunc()

def myfunc():
    x = "fantastic"
    print("Python is " + x)

myfunc()

print("Python is " + x)

def myfunc():
    global x
    x = "fantastic"

myfunc()

print("Python is " + x)