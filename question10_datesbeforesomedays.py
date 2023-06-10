from datetime import datetime  , timedelta


def final_previous_date(input_date , n):
    date = datetime.strptime(input_date , '%y-%m-%d')
    days_difference = timedelta(days = n)
    previous_date = date - days_difference
    previous_date_str = previous_date.strftime('%y-%m-%d')
    return previous_date_str

input_date = input("Enter a date in form yy-mm-dd ")
n = int(input("Enter a number which you want to subtract from input date "))
result = final_previous_date(input_date , n)
print("final date is" ,result)
