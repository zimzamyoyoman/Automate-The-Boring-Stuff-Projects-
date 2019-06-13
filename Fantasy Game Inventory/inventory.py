def displayInventory(inventory):
    print("Inventory:")
    total_items=0
    for k,v in inventory.items():
        print(str(v) + ' ' + k )
        total_items += v
    print("Total Number of Items: " + str(total_items))

def addToInventory(inventory, addedItems):
    for listItem in addedItems:
        if listItem in inventory:
            inventory[listItem]+=1
        else:
            inventory.setdefault(listItem,1)
    print("After adding items:")
    displayInventory(inventory)

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
displayInventory(stuff)

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
goblinLoot = ['gold coin', 'wine', 'grapes', 'gold chain', 'arrow']
addToInventory(stuff,dragonLoot)
addToInventory(stuff,goblinLoot)