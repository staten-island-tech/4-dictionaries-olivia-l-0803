ItemList = [{"itemName": "Magazine", "price":"$25"},
            {"itemName": "Gooner Fanfic", "price": "$35"},
            {"itemName": "Study Materials", "price": "$500"},
            {"itemName": "Teriyaki One Menu", "price": "$10"},
            {"itemName": "Three Week Old Moldy Ahh Cheese", "price": "free!"},
            {"itemName": "Monkey Comics", "price": "$50"},
            {"itemName": "7 Day Old Dead Goldfish", "price": "$72"},
            {"itemName": "Ella Jiang's Poopy Shoes", "price": "$1226"}
            ]
 
purchases = []
for i in range(0, len(ItemList)):
    purchases.append(ItemList[i]["itemName"])

print(f"Welcome to Bigbackliver's Library!! Today we have {purchases} for sale")

userWant = input("What would you like to buy? ").lower()