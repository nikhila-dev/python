import datetime 
date=str(input('Enter the date:'))
day_name= ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']
day = datetime.datetime.strptime(date, '%d %m %Y').weekday()
print(day_name[day]) 
