#Gavin Pierce

admin=["fish" ,"d0gg" , "TR33" , "0P3N" ]

user=["TREE" , "FR0G", "C@T", "M@P"]

authorized=input("what is your acount name? ")

if authorized in admin:

    print("welcome to the system all mighty ruler")
elif authorized in user:

    print("welcome user to the system")
else:

    print("you either dont have a valid acount or are baned please check with admin")