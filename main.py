def my_function():
 return 3*2


output=my_function()

print(output) 


# Functions with outputs:
def format_name(f_name,l_name):
  f_capital=f_name.title()
  l_capital=l_name.title() 

  return (f"{f_capital} {l_capital}") 
  


formated_string=format_name("sumit","SUmiT")
# used .title() function for re-arranging strings 
print(formated_string) 

# using multiple return values:

def format_name(f_name,l_name):
  
  if f_name=="" or l_name=="": 
    return
  
  
  f_capital=f_name.title()
  l_capital=l_name.title() 

  return (f"{f_capital} {l_capital}") 
  


formated_string=format_name(input("Waht is your first name ?"),input("What is your last name? "))
# used .title() function for re-arranging strings 
print(formated_string) 


