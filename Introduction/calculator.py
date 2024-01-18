# The functions are run sepratly, inner(input) first, then outer(int)
    # Float = a number with a decimal  
x = float(input("What's x? "))
y = float(input("What's y? "))

# , tells to go to the ex: secont decimal place 
z = round(x / y, 2)

# Print a , when a number goes over 3 digits ex: 1000 = 1,000
    #by using .2 insted of a , you can get the same effect (without the ", 2" in the "z = round" var)
print(f"{z:,}")