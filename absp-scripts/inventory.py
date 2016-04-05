stuff = {"rope": 1, "torch": 5, "gold coin": 42, "dagger": 1, "arrow": 12}

def display_inventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(v, k)
        item_total += v
    print("Total number of items: %s" % str(item_total))

def add_to_inventory(inventory, added_items):
    for k in added_items:
        if k in inventory.keys():
            inventory[k] += 1
        else:
            inventory.setdefault(k, 1)

inv = {"gold coin": 42, "rope": 1}
loot = ["gold coin", "dagger", "gold coin", "gold coin", "ruby"]
add_to_inventory(inv, loot)
display_inventory(inv)
