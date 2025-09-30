ItemList = [{"itemName": "Magazine", "price": 25},
            {"itemName": "Gooner Fanfic", "price": 35},
            {"itemName": "Study Materials", "price": 500},
            {"itemName": "Teriyaki One Menu", "price": 10},
            {"itemName": "Three Week Old Moldy Ahh Cheese", "price": 0},
            {"itemName": "Monkey Comics", "price": 50},
            {"itemName": "7 Day Old Dead Goldfish", "price": 72},
            {"itemName": "Ella Jiang's Poopy Shoes", "price": 1226},
            {"itemName": "Mia's Grass", "price": 120}
            ]
 
purchases = []
for i in range(0, len(ItemList)):
    purchases.append(ItemList[i]["itemName"])

print(f"Welcome to Bigbackliver's Library!! Today we have {purchases} for sale")



 

userContinue = True
Cart = []
total = 0

while userContinue:
    userItemInput = int(input("Which item do you want to buy? (Type a number): "))

    addCart = input(f"Would you like to add {ItemList[userItemInput - 1]["itemName"]} for ${ItemList[userItemInput - 1]["price"]}? ").lower()
    if addCart.__contains__("yes") or addCart.__contains__("ok"):
        Cart.append(ItemList[userItemInput-1]["itemName"])
        total += ItemList[userItemInput-1]["price"]
        print("Purchased!")
    elif  addCart.__contains__("no"):
        print("Let's put the item back. ")
    else: 
        print("Sorry, invalid answer :(")

    userItemInput = input("Would you like to continue shopping? ")
    if userItemInput.__contains__("yes") or userItemInput.__contains__("ok") or userItemInput.__contains__("continue"):
        userContinue = True 
    elif userItemInput.__contains__("no") or userItemInput.__contains__("stop"):
        print(f"You bought {Cart} and your total comes to ${total}. Thank you for shopping!")
        userContinue = False