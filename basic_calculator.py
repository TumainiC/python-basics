"""
Basic Calculator Program

Create a simple Python program that asks the user to input two numbers and a mathematical operation (addition, subtraction, multiplication, or division).
Perform the operation based on the user's input and print the result.
Example: If a user inputs 10, 5, and +, your program should display 10 + 5 = 15.
"""
valid_operators = ["+", "-", "/", "//","**","*" ]
def calculator(num1, num2, operator):
  if operator.strip() == "+":
    return num1 + num2
  elif operator.strip() == "-":
    return num1 - num2
  elif operator.strip() == "/":
    return num1 / num2
  elif operator.strip() == "//":
    return num1 // num2
  elif operator.strip() == "*":
    return num1 * num2
  elif operator.strip() == "**":
    return num1 ** num2
  else:
    print("Invalid input. Please read through valid operators")

def main():
  print("/nWelcome to calculator")
  num1 = float(input("Enter first number: "))
  num2 = float(input("Enter second number: "))
  operator = input("Enter an operator (+, -, /, //, **, *): ")
  if operator.strip() in valid_operators:
      result = calculator(num1, num2, operator)
      print(f"{num1} {operator} {num2} = {result}")
  else:
      print("Invalid operator. Please use one of the following: +, -, /, //, **, *")

if __name__ == "__main__":
    main()
