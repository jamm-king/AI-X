import datetime

now = datetime.datetime.now()
print(now)
print(now.year, now.month, now.day)
print(now.strftime("%Y년 %m월 %d일"))

# 10일 후 날짜 구하기
after_10days = now + datetime.timedelta(days=10)
print(f"10일 후 => {after_10days}")

import os

print(os.getcwd())