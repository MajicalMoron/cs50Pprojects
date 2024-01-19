#is a number even or odd
def main():
    x = int(input("What's X? "))
    if is_even(x):
        print("Even")
    else: 
        print("Odd")

def is_even(n):
    if n % 2 == 0:
        return True


main()