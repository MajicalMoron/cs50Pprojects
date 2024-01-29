#show proof that I did stuff 
# gonna be a calculator 
x = int(input("What's x? "))
y = int(input("What's y? "))
fn = input("What opperation: ").title
z = 0
name1 = "place hold"
name2 = "place hold"
name3 = "place hold"
name4 = "place hold"

opperation = [
    {"name1": "Multiplication" or "Times" or "Multiply"},
    {"name2": "Divide" or "Division" or "Over"},
    {"name3": "Subtract" or "Subtraction" or "Minus" or "Less"},
    {"name4": "Add" or "Addition" or "Plus"},
]

def equation(fn):
    if "fn" == opperation["name1"]:
        z =  x * y
    elif fn == opperation["name2"]:
        z = x / y
    elif fn == opperation["name3"]:
        z = x - y
    elif "fn" == opperation["name4"]:
        z = x + y
    return(z)
    
'''
def equation(fn):
    if fn == "Multiplication" or fn == "Times":
        print(x * y)
    elif fn == "Subtraction" or fn == "Minus":
        print(x - y)
    elif fn == "Division" or fn == "Divide":
        print(x / y)
    elif fn == "Addition" or fn == "Add":
        print(x + y)
'''
equation(fn)
print(z)
