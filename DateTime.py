import datetime,time


today = datetime.date.today()
print("Today:", today)
print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)


my_date = datetime.date(2019, 11, 4)
print(my_date)


timestamp = time.time()
print("Timestamp:", timestamp)
d = datetime.date.fromtimestamp(timestamp)
print("Date:", d)
print(d.replace(year=1992, month=1, day=16))
print(d.weekday())


t = datetime.time(14, 53, 20, 1)
print("Time:", t)
print("Hour:", t.hour)
print("Minute:", t.minute)
print("Second:", t.second)
print("Microsecond:", t.microsecond)


for i in range(6):
    print(i)
    time.sleep(1)


timestamp = 1572879180
print(time.ctime(timestamp))


print(time.gmtime(timestamp))
print(time.localtime(timestamp))
    

st = time.gmtime(timestamp)
print(time.asctime(st))
print(time.mktime((2019, 11, 4, 14, 53, 0, 0, 308, 0)))


print("today:", datetime.datetime.today())
print("now:", datetime.datetime.now())
print("utcnow:", datetime.datetime.utcnow())


d = datetime.datetime(2020, 10, 4, 14, 55)
print("Timestamp:", d.timestamp())

d = datetime.date(2020, 11, 4)
print(d.strftime('%Y/%m/%d'))
print(t.strftime("%H:%M:%S"))
print(d.strftime("%y/%B/%d %H:%M:%S"))

print(time.strftime("%Y/%m/%d %H:%M:%S", st))
print(time.strftime("%Y/%m/%d %H:%M:%S"))

print(datetime.datetime.strptime("2019/11/04 14:53:00", "%Y/%m/%d %H:%M:%S"))

d2 = datetime.date(2019, 11, 4)
print(d - d2) #Delta Object

d2 = datetime.datetime(2019, 11, 4, 14, 53, 0)
print(d - d2) #Delta Object

delta = datetime.timedelta(weeks=2, days=2, hours=2)
print(delta)
delta2 = delta * 2
print(delta2)
print(d+delta2)
print(d2+delta2)


print(my_date.strftime("%Y/%m/%d %H:%M:%S"))
print(my_date.strftime("%y/%B/%d %H:%M:%S %p"))
print(my_date.strftime("%a, %Y %b %d"))
print(my_date.strftime("%A, %Y %B %d"))
print(my_date.strftime("Weekday: %w"))
print(my_date.strftime("Day of the year: %j"))
print(my_date.strftime("Week number of the year: %W"))
    