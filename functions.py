# THE CALCULATOR APP

# Task1 create functions for each arthmertic operations
def add_numbers(a,b):
    return a + b
result = add_numbers(2, 2)
print(result)
def subtract_nums(a, b):
    return a - b
print(subtract_nums(18, 9))

def multiply_nums(a, b):
    return a * b
print(multiply_nums(5, 7))

def divide_nums(a, b):
    return a/b
print(divide_nums(20,4))


# Task2  Implement user input to receive numbers and an operation choice.
response = input("Would you like to add, subtract, multiply, or divide?")
num1 = int(input("first number? "))
num2 = int(input("second number? "))

if response == "add":
    print(num1 + num2)
elif response == "subtract":
    print(num1 - num2)
elif response == "multiply":
    print(num1 * num2)
elif response == "divide":
    print(num1 / num2)
    
#Task 3: Ensure your program can handle division by zero and other potential errors.

try: 
    if num1 == 0 or num2 == 0:
     print: 0
except (ValueError, ZeroDivisionError):
    print("Please provide two numbers and ensure that is not empty")
except Exception as e:
    print(f"An unknown error occurred: {e}")


#=============================================== 2. The Shopping List Maker================================================

# The aim of this assignment is to create a program that helps users make a shopping list.

# Task 1: Write a function that lets the user add items to a list.
# Task 2: Include a feature to remove items from the list.
# Task 3: Add a function that prints out the entire list in a formatted way.

shopping_cart = []
bagged_items = []

def add_item(cart):
    item = input("What would you like to add to your cart? ").lower() #lowercases the string
    if item not in cart:
        cart.append(item)
    else:
        print(f"{item} is already in your cart!")

def remove_item(cart):
    item = input("Which item would you like to remove from your cart?").lower()
    cart.remove(item)
    try:
         cart.remove(item)
    except ValueError:
        print(f"{item} is not in your cart, you can't remove something that doesn't exist!")


def bag_item(cart, bag):
    item = input("Which item would you like to bag?").lower()
    try:
        
        cart.remove(item)
        bag.append(item)
    except ValueError:
        print("That item is not in your cart...")

def view_items(cart, bag):
    response = input("Would you like to check your cart or your bag?").lower()
    if response == "cart":
        print("Here are your items!")
        for item in cart:
            print(item)
    elif response == "bag":
        print("Here are your purchased items: ")
        for item in bag:
            print(item)
    else:
        print("please enter a valid response!")             




def run(cart,bag):
    while True:
        response = input("What would you like to do? add/remove/purchase/view/quit").lower()
        if response == "add":
            
            add_item(cart)
            print(cart)
        elif response == "remove":
            remove_item(cart)
            print(cart)

        elif response == "purchase":
            bag_item(cart, bag)
            print("Your purchased items: ")
            for item in bag:
                print(item)
        elif response == "view":
            view_items(cart, bag)

        elif response == "quit":
            for item in cart:
                print(item)
            for purchased_item in bag:
                print(purchased_item)
            break
        else:
            print("Please enter a valid response")



run(shopping_cart, bagged_items)

