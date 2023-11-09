from datetime import datetime, timedelta

load_date = datetime.now()
print(load_date)
next_date = (load_date + timedelta(days=200))
print(next_date)
if load_date.year < next_date.year:
    print("update")
