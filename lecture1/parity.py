#is a number even or odd
def main():
    x = int(input("What's X? "))
    if is_even(x):
        print("Even")
    else: 
        print("Odd")

# universal function that tells if something is even or odd
def is_even(n):
    return True if n % 2 == 0 else False
    ''' # alternate way of saying the same thing
    if n % 2 == 0:
        return True
    else:
        return False
'''

main()