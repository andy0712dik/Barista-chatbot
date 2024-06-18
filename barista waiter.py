print("Welcome to coffe house")
name = input("what is your name\n")
menu = ("\ncoffee \nTea \nLatte")
print(name + " we are serving this " + menu)
order = input(name + " what you like to have "  )
price = 20
quantity = input("how much coffee you want \n")
total = price * int(quantity)
print("your bill is: " + str(total))

print("your " + order + " will be ready in 1 min")