# Create a function named calculate_discount(price, discount_percent) that calculates the final price after applying a discount. The function should take the original price (price) and the discount percentage (discount_percent) as parameters. If the discount is 20% or higher, apply the discount; otherwise, return the original price.
# Using the calculate_discount function, prompt the user to enter the original price of an item and the discount percentage. Print the final price after applying the discount, or if no discount was applied, print the original price.

import sys
def calculate_discount(price, discount_percent):
  discount = float(discount_percent/100)
  new_price = price - (price* discount)
  return new_price

while True:

  price = int(input("Hey there! Please enter the price of your product: "))
  discount = int(input("Now please input the discount as a percentage eg, 20, 15: "))
  print(f"Got it. So the price is {price} and the discount is {discount}%.")
  truth = input("Type 'y/n': ")

  if truth == 'y':
    final_price = calculate_discount(price, discount)
    print(f"The new price is {final_price}")
    sys.exit()
  else:
    sys.exit()
  