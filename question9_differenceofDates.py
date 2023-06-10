from datetime import datetime , timedelta

def function(from_date , to_date , difference):
    date1 = datetime.strptime(from_date , '%y-%m-%d')
    date2 = datetime.strptime(to_date , '%y-%m-%d')
    
    date_difference= date2 - date1
    
    days_given = timedelta(days = difference)
    
    if date_difference<days_given:
        return True
    else:
        return False
    
from_date  = input("Enter date 1  in form of yy-mm-dd")
to_date = input("Enter date 2 in form of yy-mm-dd")
difference = int(input("Enter no of days"))

 


print(function(from_date , to_date , difference))
