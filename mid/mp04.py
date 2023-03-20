year = int(input("년도를 입력하세요 : "))
month = int(input("월을 입력하세요 : "))
day = int(input("일을 입력하세요 : "))


def isLeapYear(year):
    
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print("True")
    else:
        print("False")
      
def getDayOfYear(year, month, day):
    dayOfYear = (month - 1) * 31 + day
    if year <= 0 or (month < 1 or month > 12):
        print("0")
    else:
        if month >= 3 and month <= 12:
            dayOfYear -= ((4 * month + 23) // 10)
            if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
                dayOfYear += 1
        print("통일: " + str(dayOfYear))
    

isLeapYear(year)

getDayOfYear(year,month,day)
