# 1
def max(a):
    max = a[0]
    for i in range(1, len(a)):
        if (a[i] > max):
            max = a[i]
    return max

a = [1, 2, 3]
print(max(a))

# 2
def getList():
    result = []
    for i in range(5):
        result.append(int(input("정수를 입력 : ")))
    return result

print(getList())

def getTuple():
    result = []
    for i in range(5):
        result.append(int(input("정수를 입력 : ")))
    result = tuple(result)
    return result

print(getTuple())

# 3
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

def coinList(count):
    front = 0
    back = 0
    for i in range(count):
        if (randint(0, 1) == 0):
            front += 1
        else :
            back += 1
    return [front , back]

coin(100)
coin(1000)
coin(10000)

count = int(input("던질 횟수 : "))
coin(count)

count = int(input("던질 횟수 : "))
print(coinList(count))

# 4
def getDivisiorList(number):
    result = []
    for i in range(1, number + 1):
        if (number % i == 0):
            result.append(i)
    return result

def getSumOfDivisiors(number):
    result = getDivisiorList(number)
    sum = 0
    for i in result:
        sum += i
    return sum

number = int(input("숫자를 입력 : "))
print(getSumOfDivisiors(number))