def is_leap(year):
  is_leap = True
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return is_leap
      else:
        return False
    else:
      return is_leap
  else:
    return False
#print(is_leap (2020))

# TODO: Add more code here 👇
def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if is_leap(year) and month == 2:
    return 29
  elif not is_leap(year) and month ==2:
    return 28
  else:
    return month_days[month-1]
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year\n")) # 
month = int(input("Enter a month\n")) # 
days_in_month(year, month)
days = days_in_month(year, month)
print(days)

