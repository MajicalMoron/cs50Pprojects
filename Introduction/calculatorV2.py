# calculator.py but using functions and perimeters for efficency 

def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n):
    # can also be done with "pow"
    return n * n

main()