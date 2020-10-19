from datetime import datetime
import pandas as pd

print('Datetime object for Jan 15 2012:')
print(datetime(2012,1,15))
print('\nSpecific')
print(datetime(2012,1,15,21,20))
print("\nlocal date and time")
print(datetime.now())
print("\nWithout time")
print(datetime.date(datetime(2012,1,15)))
print("\nCurrent date")
print(datetime.now().date())
print("\nTime from a datetime")
print(datetime.time(datetime(2012,1,15,20,15)))
print("\nCurrent local time")
print(datetime.now().time())

tday = datetime(2020, 10, 15)
print("\nCurrent date:", tday)
tomorrow = tday + pd.Timedelta(days=1)
print("tomorrow:", tomorrow)
yesterday = tday - pd.Timedelta(days=1)
print('Yesterday:', yesterday)
date1 = datetime(2020, 6, 23)
date2 = datetime(2020, 7, 16)
print("difference", (date1 - date2))


date_range = pd.date_range('2020-06-01',periods=20)
print('\nDate Range',date_range)

time_series = pd.date_range('1/1/2020',periods=20,freq='3M')
print('\nTime series',time_series)