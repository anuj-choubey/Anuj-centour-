from datetime import date, timedelta
today = date.today()

yesterday = today - timedelta(days = 1)
print(today)
print(yesterday)
