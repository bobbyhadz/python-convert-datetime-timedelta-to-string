# How to convert a datetime.timedelta to String in Python 

from datetime import datetime

start_datetime = datetime(2023, 9, 20, 8, 30)
end_datetime = datetime(2023, 9, 30, 10, 30)

time_delta = end_datetime - start_datetime

print(time_delta)  # 👉️ 10 days, 2:00:00
print(type(time_delta))  # 👉️ <class 'datetime.timedelta'>


time_delta = str(time_delta)
print(time_delta)  # 👉️ 10 days, 2:00:00
print(type(time_delta))  # 👉️ <class 'str'>