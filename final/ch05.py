# 반복문 (while 문)
sum = 0
n = 1
while n <= 10:
    sum += n
    n += 1
print(sum)

# 1~100 사이 정수 입력 받기
n = int(input("1~100 사이 정수 입력: "))
while n < 1 or n > 100:
    n = int(input("1~100 사이 정수 입력: "))

# range 문
a = range(3)	    # a = range(0, 1, 2)
a = range(1, 5)     # a = range(1, 2, 3, 4)
a = range(1, 5, 2)  # a = range(1, 3)
a = range(7, 1, -2) # a = range(7, 5, 3)

# 반복문 (for 문)
sum = 0
for i in range(10):
    sum += i
print(sum)

for i in range(1, 5, 2):  # 1 3 출력
    print(i, end = ' ')