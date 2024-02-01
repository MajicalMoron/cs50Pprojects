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

# Opperation Transvers
def opp_tr():
    p = str("place holder")
    p1 = 0
    #i = 0
    for i in range(opperation("name"[p1])):
        p = opperation["name"[i]]
        if fn == p:
            return(p)
        if i < range(opperation(p1)):
            p1 = p1 + 1
            i = 0
    

def equation():
    if fn == opperation["name"]:
        z =  x * y
        z = z + " -Multiplication"
    elif fn == opperation["name"]:
        z = x / y
        z = z + " -Division"
    elif fn == opperation["name"]:
        z = x - y
        z = z + " -Subtraction"
    elif "fn" == opperation[opp_tr()]:
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



print(opp_tr())
equation(fn)
print(z)
