food_list = []
while True:
    print("Favourite Food Manager")
    print("0. Exit")
    print("1. Add Foods")
    print("2. Remove Foods")
    print("3. View Favourite All Foods")

    choice = input("Choose an option: ")  # taken from user input

    if choice == "0":
        print("Thanks For Using Favourite Foods Manager!!!")
        break
    elif choice == "1":
        food = input("What Favourite type of food, do you want to eat?")
        food_list.append(food)
    elif choice == "2":
        delete_food = input(
            "Enter the food name you want to remove from your favorites list: "
        )
        if delete_food in food_list:
            food_list.remove(delete_food)
            print(f"{delete_food} - Removed from favorites list")
        else:
            print(f"{delete_food} - Not found in the list!")
        continue
    elif choice == "3":
        if len(food_list) == 0:
            print("Your favourite food list is empty! no food is added yet")
        else:
            print("Your favourite food list: ")
            for index, food in enumerate(food_list):
                print(f"{index+1} : {food} ")
        continue
    else:
        print("Invalid option! Please choose from the given options.")
