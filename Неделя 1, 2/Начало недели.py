from datetime import datetime, timedelta

day = input()
dt = datetime.strptime(day, '%d-%m-%Y')
start = dt - timedelta(days=dt.weekday())
print ("{:%d-%m-%Y}".format(start))