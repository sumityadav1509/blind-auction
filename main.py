def is_leap(year):
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