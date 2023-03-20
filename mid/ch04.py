# 함수 정의
def add(a, b):		# same as
    sum = a + b		# def add(a, b):
    return sum		#     return a + b
x = 5
sum = add(x, 7)
print(sum)

# 변수의 유효 범위
sum = 0
def add(a, b, c):
    global sum     # 앞에서 만들어진 sum변수를 함수 내부에서 사용하겠다는 의미
    sum = a + b + c
    print(sum)

add(3, 2, 4)
print(sum)

# return의 또 다른 사용 예
def printMinusNumber(num):
    if num >= 0:
        return # 함수를 종료한다.
    else:
        print(num)

# 재귀 호출
def factorial(n):
    if n <= 1:   # 재귀호출 탈출 조건
        return 1
    else:
        return n * factorial(n - 1)

factorial(1)               # 1
factorial(10)              # 3628800

def gcd(m, n): # 최대공약수(Great Common Denominator)
    if m == n:          
        return m      # 재귀호출 탈출 조건
    elif m > n:
        return gcd(m - n, n)
    else:           # m < n
        return gcd(m, n - m)

gcd(12, 4)                      # 4
gcd(12, 18)                     # 6

def fibonacci(n): # 피보나치 수열
    if n == 1 or n == 2:  # 재귀호출 탈출 조건
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

fibonacci(1)                   # 1
fibonacci(2)                   # 1
fibonacci(3)                   # 2
fibonacci(6)                   # 8
