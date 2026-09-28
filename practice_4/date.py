import datetime

x = datetime.datetime.now()

print(x.day - 5)

#2
import datetime

x = datetime.datetime.now()

today = x.strftime('%A')
yesterday = (x - datetime.timedelta(days=1)).strftime('%A')
tomorrow = (x + datetime.timedelta(days=1)).strftime('%A')
print(yesterday); print(today); print(tomorrow)

#3
import datetime

x = datetime.datetime.now()

print(x.strftime('%f'))


#4
from datetime import datetime

date1 = datetime(2026, 9, 28, 12, 0, 0)
date2 = datetime(2026, 9, 30, 15, 30, 45)

print(date2.timestamp() - date1.timestamp())