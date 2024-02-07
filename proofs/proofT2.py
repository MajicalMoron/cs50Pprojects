#cats that have certian features (Transversal) 

cats = [
    #Ht = hair type
    {"Name": "Dunkaroo", "Age": "Adult", "Ht": "Medium"},
    {"Name": "Termite (Smokey)", "Age": "Adult", "Ht": "Short"},
    {"Name": "Xenomorph", "Age": "Young", "Ht": "Short"},
    {"Name": "Blody Mary", "Age": "Kitten", "Ht": "Short"},
    {"Name": "Gossip Girl", "Age": "Young", "Ht": "Short"}
]
for cats in cats:
    print(cats["Name"],cats["Age"],cats["Ht"], sep= ", ")

'''
cats = [
    #attributes
    {"A1": "playful", "A2":"caring", "A3":"murderous" },
    #breed
    {"B1": "gray", "B2": "tuxedo", "B3": "ginger", "B4": "black"}
]
'''