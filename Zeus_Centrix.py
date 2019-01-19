import datetime

nowSpain = datetime.datetime.utcnow() + datetime.timedelta(hours=1) # Spain has 2 time zones - WET (UTC+0) and CET (UTC+1)
print(nowSpain.strftime("%Y-%m-%d %H:%M:%S"))