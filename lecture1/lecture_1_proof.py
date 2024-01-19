#show proof that I did stuff 
# gonna be a calculator 
x = int(input("What's x? "))
y = int(input("What's y? "))
fn = input("What opperation: ")

if fn == "Multiplication" or fn == "Times":
    print(x * y)
elif fn == "Subtraction" or fn == "Minus":
    print(x - y)
elif fn == "Division" or fn == "Divide":
    print(x / y)
elif fn == "Addition" or fn == "Add":
    print(x + y)
