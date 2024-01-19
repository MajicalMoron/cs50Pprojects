#tells what harry potter house certin charicters are in 
name = input("What's your name? ")

match name:
    # "|" is meaning "or" in this context 
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    # "_" in this context means anything else
    case _:
        print("Who?")