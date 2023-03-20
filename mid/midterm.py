# 1
Temp = float(input("온도를 입력하세요"))
Humid = float(input("습도를 입력하세요"))

DI = 0.81 * Temp + 0.01 * Humid * (0.99 * Temp - 14.3) + 46.3

if DI <= 69:
    print("쾌적함")
elif DI > 70 and DI < 80:
    print("일부사람들이 불쾌감을 느낄수 있음")
elif DI >= 80 and DI <= 83:
    print("50%정도의 사람이 불쾌감을 느낌")
elif DI > 83:
    print("대부분의 사람이 불쾌감을 느낌")

# 2
def cost(distance):
    dis = (distance / 10 * 1600) + (distance / 40 * 8350)
    return dis

def vscost():
    acost = cost(30)
    bcost = cost(50)
    acom = 1000000
    bcom = 950000
    if acom + acost < bcom + bcost:
        print("a에서 사는 것이 더 이득")
    elif acom + acost > bcom + bcost:
        print("b에서 사는 것이 더 이득")
    else:
        print("상관없음")
    print("A쇼핑몰의 컴퓨터를 제외한 나머지 비용:", acost)
    print("B쇼핑몰의 컴퓨터를 제외한 나머지 비용:", bcost)

print(vscost())

# 3
def getFirstWord(word):
    s = word.strip()
    n = s.index(' ')
    return s[:n]

def getThirdWord(str):
    str = str.strip()
    n = str.index(' ')
    str = str[n + 1: ]
    str = str.strip()
    if ' ' in str:
        n = str.index(' ')
        str = str[n + 1:]
        str = str.strip()
        if ' ' in str:
            return getFirstWord(str)
        else: 
            return str
    else:
        return ""

def getWords(str):  
    return getFirstWord(str) + " " + getThirdWord(str)

def printFirstAndThirdWords(str):
    firstWord = getFirstWord(str)
    thirdWord = getThirdWord(str)

    if thirdWord == "":
        print(firstWord)
    else:
        s = firstWord + " " + thirdWord
        print(s, len(s))

printFirstAndThirdWords("hello world ")
printFirstAndThirdWords("hello world it's a nice day")
printFirstAndThirdWords("hello      world it's a nice day")
printFirstAndThirdWords("hello world it's     a nice day     ")