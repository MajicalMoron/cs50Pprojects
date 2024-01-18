# hello.py but using/experimenting with functions and perimeters

# everything indented under "def hello():" is part of the function
    # "def" is defining the function
        # must define the function before you can call it 
    # "hello(to)" the "to" is a perimeter 
        # 'to="World"'is giving the perimeter "to" a inital value (World)
def hello(to="World"):
    print("hello,", to)

# call the function
hello()
name = input("What's your name?")
hello(name)