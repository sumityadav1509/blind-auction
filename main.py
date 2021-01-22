# Calculator 

# Add
def add(n1,n2):
  return (n1+n2)  

# Subtract 
def subtract(n1,n2):
  return (n1-n2) 

#Multiplication
def multiply(n1,n2):
  return(n1*n2) 

# Division
def division(n1,n2):
  return(n1/n2)



operations={
  "+":add,
  "-":subtract,
  "*":multiply,
  "/":division


} 
num1=int(input("What's the first number?: "))
 

# function=operations["+"]
# print(function) 
for symbol in operations:
  print(symbol)
should_continue=True 

while should_continue:

  operation_symbol=input("Pick an operation from the line above: ") 
  num2=int(input("What's the second number?:")) 
  calculation_function=operations[operation_symbol] 
  answer= int(calculation_function(num1,num2) )

  print(f"{num1}{operation_symbol}{num2}={answer}")

  if input(f"Type 'y' to continue calculating with {answer} , or type 'n' to exit : ")=="y":
    num1=answer 
  else:
    should_continue=False 
    
