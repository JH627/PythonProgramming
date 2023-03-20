year = int(input("연도를 입력하세요 : "))
month = int(input("월을 입력하세요 : "))
day = int(input("일을 입력하세요 : "))

if year % 400 == 0:
    year = 1
elif year % 4 == 0:
    if year % 100 == 0:
        year = 0
    else:
        year = 1
else:
    year = 0
    
if month >= 1 and month <= 3 :
    dayOfYear = (month - 1) * 31 + day
else:
    dayOfYear = ((month - 1) * 31 + day) - ((4 * month + 23)// 10) + year

print(dayOfYear)
