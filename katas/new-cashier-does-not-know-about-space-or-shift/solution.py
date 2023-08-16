def get_order(order):
    menu = ["Burger", "Fries", "Chicken", "Pizza", "Sandwich", "Onionrings", "Milkshake", "Coke"]
    order_list = []
    for item in menu:
        order_list += [item] * order.count(item.lower())
    
    return " ".join(order_list)