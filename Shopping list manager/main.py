#Gavin Pierce Shopping list manager

shoppingList= ["start", ]

while True:

    action = input("""What would you like to do?
                   
                                  Enter 1 to add item
                   
                                  Enter 2 to remove item
                   
                                  Enter 3 to leave the list:\n""")
    
    if action =="1":

        itemAdd=input("what would you like to add? ")

        shoppingList.insert(1, itemAdd)

        print (shoppingList)


    elif action =="2":

        itemRemove=input("what would you like to remove ")

        shoppingList.remove(itemRemove)

        print (shoppingList)

    else:

        print("Have a nice day!")

        break