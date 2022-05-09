import random

destinations = ["Santa Barbara, California", "Tulum, Mexico", "Las Vegas, Nevada", "London, England"]
random_destinations = random.choice(destinations)
print(random_destinations)

transportation = ["Helicopter", "Private Jet", "Charter Bus", "Limo Service"]
random_transportation = random.choice(transportation)
print(random_transportation)

restaurants = ["Olive Garden", "Chuy's Tex-Mex", "Nick and Sam's Steakhouse", "Fadi's Mediterranean Grill"]
random_restaurants = random.choice(restaurants) # random generater
print(random_restaurants)

entertainment = ["Cirque du Soleil", "Tour the City's Main Attractions", "Zip-lining", "Cliff Jumping"]
random_entertainment = random.choice(entertainment)
print(random_entertainment) 


Satisfied = input("Would you like to proceed?: ")
if Satisfied == "Yes":
    print(f"Congratulations, you're going to {random_destinations} ")
elif Satisfied == "Reshuffle":
    Reshuffle = input("Which category would you like to reshuffle?: ")
    if Reshuffle == "Destinations":
        random_destinations = random.choice(destinations)
        print(random_destinations)
    elif Reshuffle == "Transportation":
        random_transportation = random.choice(transportation)
        print(random_transportation)
    elif Reshuffle == "Restaurants":
        random_restaurants = random.choice(restaurants)
        print(random_restaurants)
    elif Reshuffle == "Entertainment":
        random_entertainment = random.choice(entertainment)
        print(random_entertainment)

     
# Looping Until User is Satisfied

def Reshuffle 
    while user_input = "Reshuffle":





