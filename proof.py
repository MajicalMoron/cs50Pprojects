#show proof that I did stuff 
# gonna be a calculator 
x = int(input("What's x? "))
y = int(input("What's y? "))
fn = input("What opperation: ").title
'''
opperation = [
    {"name": "Multiplication" or "Times" or "Multiply"},
    {"name": "Divide" or "Division" or "Over"},
    {"name": "Subtract" or "Subtraction" or "Minus" or "Less"},
    {"name": "Add" or "Addition" or "Plus"},
]'''

# making the array of lists, for each type of (basic) math problem
opperation = [
    {"multi": "Multiplication" or "Times" or "Multiply"},
    {"divi": "Divide" or "Division" or "Over"},
    {"sub": "Subtract" or "Subtraction" or "Minus" or "Less"},
    {"add": "Add" or "Addition" or "Plus"}
]

''' 
opp_pt2 = {
    "mult" : multi,
    "divi" : divi,
    "sub" : sub,
    "add" : add
}

print(opp_pt2)
'''

# Opperation Transvers
def opp_tr(p): 
    for i in opperation[p]:
        r = opperation[p, i]
        if fn == r:
            return(r)

# checks if the users input is a usable argument
if fn == opperation[0]:
    fn = opp_tr("mult")
elif fn == opperation["divi"]:
    fn = opp_tr("divi")
elif fn == opperation["sub"]:
    fn = opp_tr("sub")
elif fn == opperation["add"]:
    fn = opp_tr("add")
elif fn != opperation:
    print("Your a falure of a person. \n" + "Have a great day!")

# does the actual math problem
def equation():
    z = 0
    if fn == opperation["mult"]:
        z =  x * y
        z = z + " -Multiplication"
    elif fn == opperation["divi"]:
        z = x / y
        z = z + " -Division"
    elif fn == opperation["sub"]:
        z = x - y
        z = z + " -Subtraction"
    elif "fn" == opperation["add"]:
        z = x + y
        z = z + " -Addition"
    else:
        z = "Your a falure.\n" + "Thanks for trying tho"
    return(z)
    


    def equation(fn):
        if fn == "Multiplication" or fn == "Times":
            print(x * y)
        elif fn == "Subtraction" or fn == "Minus":
            print(x - y)
        elif fn == "Division" or fn == "Divide":
            print(x / y)
        elif fn == "Addition" or fn == "Add":
            print(x + y)



print(equation())

