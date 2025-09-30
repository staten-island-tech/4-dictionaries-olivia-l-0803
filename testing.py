userItemInput = input("string: ") 
# input()
print(type(userItemInput))
userItemInput = int(input("integer ")) 
# input()
print(type(userItemInput))




test = input('Type something largeling ')

if test.__contains__('biggie'):
    print("die kill your")
else:
    print("biggie")

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

while True:
    userItemInput = int(input("Which item do you want to buy? (Type a number): "))

    addCart = input(f"Would you like to add {ItemList[userItemInput - 1]["itemName"]} for ${ItemList[userItemInput - 1]["price"]}? ").lower()
    if addCart.__contains__("yes"):
        print("Purchased!")
    elif  addCart.__contains__("no"):
        print("Let's put the item back. ")
    else: 
        print("Sorry, invalid answer :(")
 