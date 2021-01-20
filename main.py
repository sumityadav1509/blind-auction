def is_leap(year):
  """This function is created to check the conditions if a given year is leap or not . """
  if year%4==0:
    if year%100==0:
      if year%400==0:
        # print("Leap Year")
        return True
      else:
        # print("Not Leap Year")
        return False
    else:
      # print("Leap Year")
      return True
  else:
    # print("Not Leap Year")
     return False


def day_in_month(year,month):
  """This function is created to calculate the number of days in february and provide a return value as a output from the function"""
  if month>12 or month<1:
    return "Invalid Input"
  
  month_days=[31,28,31,30,31,30,31,31,30,31,30,31] 
  if is_leap(year) and month==2:
    return 29 
  return month_days[month-1]  


year=int(input("Enter a year: "))
month=int(input("Enter a month: ")) 

days=day_in_month(year,month) 
print(days)