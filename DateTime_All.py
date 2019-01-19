import datetime
import pytz

""" DATE """
d = datetime.date(2018,7,28)    # Integer argument should not have leading zeros
print(d)
today = datetime.date.today()
print(today)    # <class 'datetime.date'>
print(today.day,today.month,today.year)
print(today.strftime("%Y-%m-%d %H:%M:%S"))
print(today.weekday())  # Monday to Sunday (0 to 6)
print(today.isoweekday())   # Monday to Sunday (1 to 7)

tdelta = datetime.timedelta(weeks=1)
print(tdelta)
print(tdelta.total_seconds())
print(today + tdelta)

# date = date +/- timedelta
# timedelta = date +/- date

""" TIME """

t = datetime.time(9,30,45,12342)
print(t)
print(t.hour)

""" DATETIME """

dt = datetime.datetime(1993,1,28,23,30,0,100000)
print(dt,dt.date(),dt.time())

dt_today = datetime.datetime.today()    # no option for argument with time zone
dt_now = datetime.datetime.now()    # Option of timezone available
dt_utcnow = datetime.datetime.utcnow()
print(dt_today,";;;",dt_now,";;;",dt_utcnow)

dt = datetime.datetime(2016,12,23,13,23,56,tzinfo=pytz.UTC)
print(dt)
dt_now = datetime.datetime.now(tz=pytz.UTC)
print(dt_now)

# dt_delhi = dt_now.astimezone(pytz.timezone("Asia/India"))
# print(dt_delhi)




d = datetime.datetime.utcnow()
e = datetime.datetime(1970,1,1)
td = d - e
print(round(td.total_seconds()))