# Write a Python scriot to print
#1. current date and TimeoutError
#2. current year
#3. month of year
#4. week number of the year
#5. weekday of the weekday
#6. day of the year
#7. day of the month
#8. day of the week 

# using built in module datetime and time 
from datetime import datetime


now  = datetime.now()
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

days = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

print(now)
print(now.year)
print(months[now.month-1])
print(now.isocalendar()[1])
print(days[now.weekday()])
print(now.timetuple().tm_yday)
print(now.timetuple().tm_mday)
print(now.timetuple().tm_wday)
