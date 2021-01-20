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
  
print(formated_string)


# format_name("sumit","SUMIT")