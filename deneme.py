age = input("Are you a cigarette addict older than 75 years old").capitalize()
chronic = input("Do you have a severe chronic disease?").capitalize()
immune = input("Is your immune system too weak").capitalize()
Yes = True
No = False
if age and chronic and immune:
   print("You are in risky group")
else:
    print("You are not in risky group")