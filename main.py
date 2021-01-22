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

operation_symbol=input("Pick an operation from the line above: ") 
num2=int(input("What's the second number?:")) 
calculation_function=operations[operation_symbol] 
first_answer= int(calculation_function(num1,num2) )

print(f"{num1}{operation_symbol}{num2}={first_answer}")

# Debugging required:
operation_symbol=input("Pick another operation: ")
num3= int(input("What's the next number ? "))
calculation_function=operations[operation_symbol]
second_answer=calculation_function(first_answer ,num3) 
print(f"{first_answer}{operation_symbol}{num3}={second_answer}")
