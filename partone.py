
ItemList = [{"itemName": "Gooner Fanfic", "price": "$35"},
            {"itemName": "Study Materials", "price": "$500"},
            {"itemName": "Teriyaki One Menu", "price": "$10"},
            {"itemName": "Three Week Old Moldy Ahh Cheese", "price": "Freebie!"}
            ]
 
purchases = ["Gooner Fanfic", "Study Materials", "Teriyaki One Menu", "Three Week Old Moldy Ahh Cheese"]

print(f"Welcome to Bigbackliver's Library!! Today we have {purchases[0]}, {purchases[1]}, {purchases[2]}, and {purchases[3]}  for sale.")

userWant = input("What would you like to buy?")




if userWant == "Gooner Fanfic" or "gooner fanfic" or "item 1":
    print(f"Let's buy {ItemList[0]['itemName']} for {ItemList[0]['price']}?")
elif userWant == "Study Materials":
    print(f"Let's buy {ItemList[1]['itemName']} for {ItemList[1]['price']}?")
elif userWant == "Teriyaki One Menu":
    print(f"Let's buy {ItemList[2]['itemName']} for {ItemList[2]['price']}?")
elif userWant == "Three Week Old Moldy Ahh Cheese":
    print(f"Let's buy {ItemList[3]['itemName']} for {ItemList[3]['price']}?")