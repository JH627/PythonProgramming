def readNumber():
    a = int(input("2이상의 정수 입력:"))
    while a<2:
        a = int(input("2이상의 정수 입력:"))
    return a

def printDivisor(num):
    for i in range(1,num+1):
        if (num % i) == 0:
            print (i)
            
num = readNumber()

printDivisor(num)