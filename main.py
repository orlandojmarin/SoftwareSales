# A software company sells a package that retails for $99. Quantity discounts
# are given according to the following table:
# Quantity 10-19, Discount 20%
# Quantity 20-49, Discount 30%
# Quantity 50-99, Discount 40%
# Quantity 100 or more, Discount 50%
# Write a program that asks the user to enter the number of packages purchased.
# The program should then display the amount of the discount (if any) and
# the total amount of the purchase after the discount

# original price variable
original_package_price = 99

# discount variables
fifty_percent_discount = 0.50
forty_percent_discount = 0.60
thirty_percent_discount = 0.70
twenty_percent_discount = 0.80
zero_percent_discount = 0

# get user input (int) for number of packages purchased
number_packages = int(input("How many packages were purchased? "))

if number_packages <= 0:
    print("Please enter a number greater than 0 to see your total.")
    number_packages = int(input("How many packages were purchased? "))

# calculate the non-discounted price
non_discounted_price = original_package_price * number_packages
total_before_discount = number_packages * original_package_price

# calculate the discount amount and total based on number of packages purchased
if (number_packages >= 100):
    discounted_package_price = original_package_price * fifty_percent_discount
    total_after_discount = number_packages * discounted_package_price
    print(f"Your discount amount is {(1-fifty_percent_discount) * 100:.0f}%")
    print(f"The total after the discount is ${total_after_discount:.2f}.")
    print(f"You saved ${total_before_discount - total_after_discount:.2f} today!")
        
elif (number_packages >= 50):
    discounted_package_price = original_package_price * forty_percent_discount
    total_after_discount = number_packages * discounted_package_price
    print(f"Your discount amount is {(1-forty_percent_discount) * 100:.0f}%")
    print(f"The total after the discount is ${total_after_discount:.2f}.")
    print(f"You saved ${total_before_discount - total_after_discount:.2f} today!")
    
elif (number_packages >= 20):
    discounted_package_price = original_package_price * thirty_percent_discount
    total_after_discount = number_packages * discounted_package_price
    print(f"Your discount amount is {(1-thirty_percent_discount) * 100:.0f}%")
    print(f"The total after the discount is ${total_after_discount:.2f}.")
    print(f"You saved ${total_before_discount - total_after_discount:.2f} today!")
    
elif (number_packages >= 10):
    discounted_package_price = original_package_price * twenty_percent_discount
    total_after_discount = number_packages * discounted_package_price
    print(f"Your discount amount is {(1-twenty_percent_discount) * 100:.0f}%")
    print(f"The total after the discount is ${total_after_discount:.2f}.")
    print(f"You saved ${total_before_discount - total_after_discount:.2f} today!")
    
else:
    print(f"Your discount amount is {zero_percent_discount}%")
    print(f"Your total is ${non_discounted_price:.2f}.")
