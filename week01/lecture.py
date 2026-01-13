menu = {
    "Shrimp Bowl": 3.99,
    "Chicken Bowl": 5.99,
    "Salmon Bowl": 6.20
}
def get_price_safe(itemName):
    return menu.get(itemName)
def get_price_unsafe(itemName):
    return menu[itemName]

print(get_price_safe("Shrimp Bowl"))

print(get_price_unsafe("Shrimp Bowl"))

def update_price_safe(itemName, price):
    if menu.get(itemName):
        menu[itemName] = price
        print(f"Price for {itemName} has been updated to {menu.get(itemName)}.")
update_price_safe("Shrimp Bowl", 4.11)

print(get_price_safe("Shrimp Bowl"))

def add_item(itemName, price):
    menu[itemName] = price
    if menu.get(itemName):
        print(f"{itemName} was added with a price of {menu.get(itemName)}")

add_item("Dr Pepper 12oz", 2.30)
print(menu)

def remove_item(itemName):
    if menu.get(itemName):
        del menu[itemName]
    print(f"{itemName} has been removed from the menu.")
remove_item("Salmon Bowl")
print(menu)