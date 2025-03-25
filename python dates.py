# python dates
from datetime import date, timedelta, datetime

today = date.today()
print(today.weekday())
f_date = today.strftime("%d/ %m/ %Y")
print(f_date)

expiry_date = today - timedelta(days=30)
print(expiry_date)

#define two dates
date1 = datetime(2005, 1, 16)
date2 = datetime(2007, 8,  15)


#calculate the diff
diff = date2 - date1
print(diff.days)












