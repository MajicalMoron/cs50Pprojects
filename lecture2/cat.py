# while and for loops
def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n?"))
        if n > 0:
            return n 

def meow(n):
    for _ in range(n):
        print("meow")

main()
'''
# delibrate infinate loop
while True:
    n = int(input("What's n ?"))
    if n > 0:
        break

for _ in range(n):
    print("meow")


print("Meow\n" * 3, end="")


# the "[]" constitute's a list 
for i in [0, 1, 2]:
    print("Meow")

i = 3
while i != 0:
    print("Meow")
    i = i - 1 
    '''