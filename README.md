Barista chatbot 
Welcome to the Coffee House!

This project is a simple command-line interface for a coffee shop. It allows customers to place an order and calculates the total bill.

How to Use
Run the script and follow the prompts.
Enter your name when asked.
Choose from the menu options: coffee, tea, or latte.
Enter the quantity of your chosen drink.
The script will calculate the total bill and display it.
Your order will be ready in 1 minute!
Code Overview
The script uses Python to:

Greet the customer and ask for their name.
Display the menu options.
Ask the customer to choose an item from the menu.
Ask for the quantity of the chosen item.
Calculate the total bill based on the price (fixed at $20) and quantity.
Display the total bill and a message indicating when the order will be ready.
Example Output
Here's an example of what the output might look like:


Verify

Open In Editor
Edit
Copy code
Welcome to Coffee House
what is your name
John
John we are serving this 
coffee 
Tea 
Latte
John what you like to have 
coffee
how much coffee you want 
2
your bill is: 40
your coffee will be ready in 1 min
Note
This is a simple script and does not include any error handling or validation. It's meant to be a fun example of a command-line interface, but it's not intended for production use.




Answer with Web Search
Continue

print("Hello welcome to Coffee house ") name = input("what is your name: ") if name == "Loki": print("Dont try to Come in Evil Loki") exit() if name == "ben" or name == "yog": evil = input("are you evil ") good_deeds = int(input("how many good did have you done today")) if evil == "yes" and good_deeds < 4: print("get out you evil " + name) exit() else: print("sorry for asking you can go " + name)

else: print("Welcome to Coffee House " + name )

menu = "Coffee\nTea\nBlack Tea\nBlack coffee\nCold Coffee" print("what would you like to have " + name + " today we are serving this \n" + menu) order = input("what would you like to have " + " " +name +" ") quantity = int(input("how much " +" "+ order +" ")) if order == "Coffee": price = 20

elif order == "Tea": price = 10 elif order == "Black Tea": price = 15 elif order == "Black Coffee": price = 25 elif order == "Cold Coffee": price = 45 cream = input("do you want Ice Cream ") if cream == "yes": price = 60 else: price = 45

else: print("sorry we dont have that one")

total = price * int(quantity) print(total) create a README.md for this code


Here is a possible README.md file for your project:

Coffee House
Welcome to the Coffee House!

This project is a simple command-line interface for a coffee shop. It allows customers to place an order, and calculates the total bill. But be warned, we have some special rules for certain customers...

How to Use
Run the script and follow the prompts.
Enter your name when asked.
If you're Loki, don't even think about trying to come in.
If you're Ben or Yog, be prepared to answer some questions about your moral character.
Choose from the menu options: Coffee, Tea, Black Tea, Black Coffee, or Cold Coffee.
Enter the quantity of your chosen drink.
If you order Cold Coffee, you'll be asked if you want Ice Cream.
The script will calculate the total bill and display it.
Special Rules
If your name is Loki, you're not allowed in.
If your name is Ben or Yog, you'll be asked if you're evil and how many good deeds you've done today. If you're evil and haven't done at least 4 good deeds, you're not allowed in.
Menu and Prices
Coffee: $20
Tea: $10
Black Tea: $15
Black Coffee: $25
Cold Coffee: $45 (or $60 with Ice Cream)
Code Overview
The script uses Python to:

Greet the customer and ask for their name.
Check for special rules based on the customer's name.
Display the menu options.
Ask the customer to choose an item from the menu.
Ask for the quantity of the chosen item.
Calculate the total bill based on the price and quantity.
Display the total bill.
Example Output
Here's an example of what the output might look like:


Verify

Open In Editor
Edit
Copy code
Hello welcome to Coffee house 
what is your name: John
Welcome to Coffee House John
what would you like to have John today we are serving this 
Coffee
Tea
Black Tea
Black coffee
Cold Coffee
what would you like to have John 
Coffee
how much Coffee 
2
60
Note
This is a simple script and does not include any error handling or validation. It's meant to be a fun example of a command-line interface, but it's not intended for production use.
