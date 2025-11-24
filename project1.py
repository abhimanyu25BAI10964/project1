#define the menu
menu = {
    'pizza':180,
    'burger':100,
    'coke':80,
    'salad':120,
    'pasta':150,
    'coffee/tea':50,
    'frenchfries':120,
    'chickenbiryani':500,
}

print("welcome to our restaurant")
print("pizza: Rs180\nburger: Rs100\ncoke: Rs80\nsalad: Rs120\npasta: Rs150\ncoffee/tea: Rs50\nfrenchfries: RS120\nchickenbiryani: Rs500")

order_total = 0

item_1 = input("What item do you want to order? =")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"your item {item_1} has been added to your order")
else:
    print(f"Sorry, {item_1} isn't available")

another_order = input("do you want to order an another item? (yes/no) ")
if another_order == "yes":
    item_2 = input("What item do you want to order? =")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"your item {item_2} has been added to your order")
    else:
        print(f"Sorry, {item_2} isn't available")
print(f"your total order is: {order_total}")