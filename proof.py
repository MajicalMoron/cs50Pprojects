#show proof that I did stuff 
# gonna be a calculator 
x = int(input("What's x? "))
y = int(input("What's y? "))
fn = input("What opperation: ").title
z = 0

opperation = [
    {"name": "Multiplication" or "Times" or "Multiply"},
    {"name": "Divide" or "Division" or "Over"},
    {"name": "Subtract" or "Subtraction" or "Minus" or "Less"},
    {"name": "Add" or "Addition" or "Plus"},
]


def equation(fn):
    if fn == opperation["name"[range()]]:
        z =  x * y
        z = z + " -Multiplication"
    elif fn == opperation["name",2]:
        z = x / y
        z = z + " -Division"
    elif fn == opperation["name"]:
        z = x - y
        z = z + " -Subtraction"
    elif "fn" == opperation["name"]:
        z = x + y
        z = z + " -Addition"
    else:
        z = "Your a falure."
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
'''
# Opperation Transvers
def opp_tr():
    for i in range(opperation):
        if i < range(opperation()):

        print(opperation(i))
'''
#opp_tr()
equation(fn)
print(z)
