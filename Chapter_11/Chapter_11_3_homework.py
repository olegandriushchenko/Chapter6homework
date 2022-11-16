from datetime import datetime

date_string = input(" enter the date in specified format - YYYY-MM\n")
print(date_string)

try:
    user_date = datetime.strptime(date_string, "%Y-%m-%d")
    print(user_date.strftime("%A"))
except ValueError:
    print("the format of the date entered is not correct")


