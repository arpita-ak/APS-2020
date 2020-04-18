def WhichDay(day,month,year):
    t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    year -= month < 3
    d = (year + int(year/4) - int(year/100) + int(year/400) + t[month-1] + day) % 7
    week = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    return week[d]

d=6
m=10
y=1998
print(WhichDay(d,m,y))