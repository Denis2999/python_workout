import datetime

y, m, d = map(int, input().split())
n_days = int(input())

date = datetime.date(y, m, d) + datetime.timedelta(days=n_days)

print(date.strftime("%Y %-m %-d"))
