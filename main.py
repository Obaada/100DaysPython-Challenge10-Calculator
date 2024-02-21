from art import logo
print(logo)
# Calculator

#add
def add(n1, n2):
  return n1 + n2

# subtract
def subtract(n1 ,n2):
  return n1 - n2

# Multiply 
def multiply(n1, n2):
  return n1 * n2

# Divide 
def divide(n1, n2):
  return n1 / n2

Operations ={
  "-": subtract ,
  "+": add ,
  "/":divide ,
  "*":multiply 
}


def calculater():
  num1 = float(input("What's the first number?: "))
  for key in Operations:
    print(key)
  
  KeepGoing = True
  while KeepGoing:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    Operation_function = Operations[operation_symbol]
    answer = round(Operation_function(num1, num2), 2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    KeepGoing = input(f"Type 'y' to continue calculating with {answer} or type 'n' to start again:")
    if KeepGoing == "n":
      KeepGoing = False
      calculater()
    else:
      num1 = answer
  
calculater()