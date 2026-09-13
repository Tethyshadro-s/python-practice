#concession stand program using dictionaries.
menu = {"pizza":199,
        "nacho":129,
        "burger":159,
        "sprite":49,
        "coke":49,
        "fries":99}

cart= []
total = 0

print("----------MENU----------")

for key, value in menu.items():
    print(f"{key:10}:{value:.2f}")

print("------------------------")

while True:
    food = input("Select an item (q to quit):").lower()
    if food == "q":
       break

    elif menu.get(food) is not None:
        cart.append(food)
    else:
        print("This item is not on the menu!!")

for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print() 
print(f"Total is: {total}")