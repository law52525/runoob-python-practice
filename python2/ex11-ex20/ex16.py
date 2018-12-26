from datetime import datetime, timedelta

date = datetime.now()
print(date.strftime("%Y/%m/%d"))  # 圣诞节
print(date.replace(day=1).strftime("%Y/%m/%d"))
print((date + timedelta(days=+1)).strftime("%Y/%m/%d"))
print((date + timedelta(weeks=+1)).strftime("%Y/%m/%d"))  # 元旦节
