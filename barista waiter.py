print("Hello  welcome to Coffee house ")
name = input("what is your name: ")
if name == "Loki":
    print("Dont try to Come in Evil Loki")
    exit()
if name == "ben" or name == "yog":
    evil = input("are you evil ")
    good_deeds = int(input("how many good did have you done today"))
    if evil == "yes" and good_deeds < 4:
        print("get out you evil " + name)
        exit()
    else:
        print("sorry for asking you can go " + name)
        
else:
    print("Welcome to Coffee House " + name )
    
menu = "Coffee\nTea\nBlack Tea\nBlack coffee\nCold Coffee"
print("what would you like to have " + name + " today we are serving this \n" + menu)
order = input("what would you like to have " + " " +name +" ")
quantity = int(input("how much " +" "+ order +" "))
if order == "Coffee":
    price = 20
    
elif order == "Tea":
    price = 10
elif order == "Black Tea":
    price = 15
elif order == "Black Coffee":
    price = 25
elif order == "Cold Coffee":
    price = 45
    cream = input("do you want Ice Cream ")
    if cream == "yes":
        price = 60
    else:
        price = 45
    

    
else:
    print("sorry we dont have that one")
 

total = price * int(quantity)
print(total)


