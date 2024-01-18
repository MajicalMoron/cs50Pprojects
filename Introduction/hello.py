# Ask the user their name. By adding strip and title we are able to concoladate some of the code 
name = input("what's your name? ") .strip().title()

'''
 Remove blankespace from str and capitalize user's name
name = name.strip().title()
'''

#split users name into first and last name
first, last = name.split(" ")
# Say hello to user
print(f"Hello, {first}")
    #using f makes python realise that whats in the {___} is actualy a vairiable 