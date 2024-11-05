menu = {
    'samosa':5,
    'cheese pizza':200,
    'chicken pizza':500,
    'veg pizza':100,
    'coca cola':40,
    'sprite':20,
    'momos(3 piece)':10,
    'veg chowmein':20,
    'chicken chowmein':30,
    'pasta':50,
    'burger':60,
}
#greet
print("Welcome To VIKALP Restaurent")
print("samosa: Rs5\ncheese pizza: Rs200\nchicken pizza: Rs500\nveg pizza: Rs100\ncoca cola: Rs40\nsprite: Rs20\nmomos (3 piece): Rs10\nveg chowmein: Rs20\nchicken chowmein : Rs30\npasta: Rs50\nburger: Rs60")

order_total = 0

item_1 = input("Enter The Name Of Item You Want To Order = ")
if item_1 in menu:
    order_total += menu[item_1] #0 + price of item that user ordered
    print(f"your item {item_1} has been added to your order")

else:
    print(f"Ordered item {item_1} is not in our restaurent")

another_order = input("Do you want to order another item? (yes/no)")
if another_order == "yes":
    item_2 = input("Enter the name of second item = ")
    if item_2 in menu:
        order_total += menu[item_2] #0 + price of item that user ordered
        print(f"your item {item_2} has been added to your order")
    else:
        print(f"ordered item {item_2} is not in our restaurent")

print(f"The total amount of item to pay is {order_total}")