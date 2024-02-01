#show proof that I did stuff 
# gonna be a calculator 
x = int(input("What's x? "))
y = int(input("What's y? "))
fn = input("What opperation: ").title
z = 0
'''
opperation = [
    {"name": "Multiplication" or "Times" or "Multiply"},
    {"name": "Divide" or "Division" or "Over"},
    {"name": "Subtract" or "Subtraction" or "Minus" or "Less"},
    {"name": "Add" or "Addition" or "Plus"},
]'''

# making the array of lists, for each type of (basic) math problem
opperation = {
    "mult": "Multiplication" or "Times" or "Multiply",
    "divi": "Divide" or "Division" or "Over",
    "sub": "Subtract" or "Subtraction" or "Minus" or "Less",
    "add": "Add" or "Addition" or "Plus",
}

# Opperation Transvers
def opp_tr(p): 
    for i in range(opperation[p]):
        r = opperation[p, i]
        if fn == r:
            return(r)

# checks if the users input is a usable argument
if fn == opperation["multi"]:
    opp_tr("multi")
elif fn == opperation["divi"]:
    opp_tr("divi")
elif fn == opperation["sub"]:
    opp_tr("sub")
elif fn == opperation["add"]:
    opp_tr("add")
else:
    print("Your a falure of a person. \n" + "Have a great day!")

# does the actual math problem
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
        z = "Your a falure.\n" + "Thanks for trying tho"
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

opp_tr()
print(equation(fn))

