# user will chose from a range of films

films = {
    "Finding Dory":[3,5],
    "Bourne":[18,5],
    "Django":[15,5],
    "Ghost Busters":[12,5],
    }

# user will pick a film

while True:
    choice = input("What film would you like to watch?: ").strip().title()

    if choice in films:
        age = int(input("How old are you?: ").strip())

        #check user age

        if age >= films[choice][0]:
            #check enough seats available

            if films[choice][1] > 0:
                print("Enjoy the film!")
                films[choice][1] = films[choice][1] - 1
                
            else:
                print("Sorry, we are sold out..")
                
        else:
            print("You are too young to see that film.")
            
    else:
        print("We don't have that film...")

