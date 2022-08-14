def is_leap(year):
    """ A function to decide whether the year is leap or not. Returns true or false"""
    if year % 4 == 0:
        if year % 100 == 0:
          if year % 400 == 0:
            return True
          else:
            return False
        else:
          return True
    else:
        return False

def days_in_month(y,m):
    """ A function to return  the days of the month, taking into consideration whether the year is leap or not""" 
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
    m -=1
    if is_leap(y) and m ==1:
        return 29
    else:
        return month_days[m]
  
  
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)










