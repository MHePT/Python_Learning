import calendar,datetime


year = datetime.date.today().year
calendar.prcal(year)
print(calendar.month(year, 11))
calendar.setfirstweekday(calendar.SUNDAY)
calendar.prmonth(year, 12)


print(calendar.weekheader(6))
print(calendar.isleap(year))
print(calendar.leapdays(2010, 2021))  # Up to but not including 2021.


c = calendar.Calendar(2)
 
for weekday in c.iterweekdays():
    print(weekday, end=" ")
# Result: 2 3 4 5 6 0 1






class MyCalendar(calendar.Calendar):
    def count_weekday_in_year(self, year, weekday):
        current_month = 1
        number_of_days = 0
        while (current_month <= 12):
            for data in self.monthdays2calendar(year, current_month):
                if data[weekday][0] != 0:
                    number_of_days = number_of_days + 1

            current_month = current_month + 1
        return number_of_days

my_calendar = MyCalendar()
number_of_days = my_calendar.count_weekday_in_year(2019, calendar.MONDAY)

print(number_of_days)
