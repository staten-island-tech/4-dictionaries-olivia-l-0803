ItemList = [{"itemName": "Magazine", "price": 25},
            {"itemName": "Gooner Fanfic", "price": 35},
            {"itemName": "Study Materials", "price": 500},
            {"itemName": "Teriyaki One Menu", "price": 10},
            {"itemName": "Three Week Old Moldy Ahh Cheese", "price": "free!"},
            {"itemName": "Monkey Comics", "price": 50},
            {"itemName": "7 Day Old Dead Goldfish", "price": 72},
            {"itemName": "Ella Jiang's Poopy Shoes", "price": 1226}
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

    addCart = input(f"Would you like to add {ItemList[userItemInput]["itemName"]} for ${ItemList[userItemInput]["price"]}? ").lower()
    if addCart == "yes" or addCart == "ok" or addCart == "okay":
        Cart.append(ItemList[userItemInput])
        total += ItemList[userItemInput]["price"]
        print("Purchased!")
    elif  addCart == "no" or addCart == "no thanks" or addCart == "no thank you":
        print("Let's put the item back. ")
    else: 
        print("Sorry, invalid answer :(")

    userItemInput = input("Would you like to continue shopping?")
    if userItemInput == "yes" or userItemInput == "okay" or userItemInput == "continue":
        userContinue = True 
    elif userItemInput == "no" or userItemInput == "no thanks" or userItemInput == "stop":
        print("Your total comes to Thank you for shopping!")