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

userItemInput = int(input("Which item do you want to buy? (Type a number): "))

 

userContinue = True
Cart = []

while userContinue:
    addCart = input(f"Would you like to add {ItemList[userItemInput]["itemName"]}? ").lower()
    if addCart == "yes" or addCart == "ok" or addCart == "okay":
        Cart.append(ItemList[userItemInput])
        print("Purchased!")
    elif  addCart == "no" or addCart == "no thanks" or addCart == "no thank you":
        print("Let's put the item back. ")
    else: 
        print("Sorry, invalid answer :(")