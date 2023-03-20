# 1
def getBiggestNumber():
    m = int(input("정수 한 개를 입력하세요: "))

    for i in range(4):
        n = int(input("정수 한 개를 입력하세요: "))
        if m < n:
            m = n
    return m

print(getBiggestNumber())

# 2
from random import randint

def coin(count):
    front = 0
    back = 0
    for i in range(count):
        if (randint(0, 1) == 0):
            front += 1
        else :
            back += 1
    print("front : ", front)
    print("back : ", back)

coin(100)
coin(1000)
coin(10000)

# 3
def getSumOfDivisiors(number):
    result = 0
    for i in range(1, number + 1):
        if (number % i == 0):
            result += i
    return result

number = int(input("숫자 입력 : "))
print(getSumOfDivisiors(number))

# 4
max = int(input("숫자 입력 : "))
if (max != 1000):
    while (True):
        num = int(input("숫자 입력 : "))
        if (num > max):
            max = num
        if num == 1000:
            break

print(max)