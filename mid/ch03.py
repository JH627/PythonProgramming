# 비교 연산자
a = 5
b = 3
print(a == b)
print(a != b)
print(a > b)
print(a >= b)
print(a < b)
print(a <= b)

# 조건문 (if 문)
if True:
    print("True")

i = 0
if i:
    print("False")

num = 5
if num >= 5:
    print("5보다 크거나 같습니다.")
if num < 5:
    print("5보다 작습니다.")

# 조건문 (if-else 문)
num = 5
if num >= 5:
    print("5보다 크거나 같습니다.")
else:
    print("5보다 작습니다.")

num = 7
if num >= 10:
    print("10보다 크거나 같습니다.")
if 5 <= num < 10:
    print("5보다 크거나 같지만 10보다 작습니다")
if num < 5:
    print("5보다 작습니다")

# 조건문 (elif 문)
num = 7
if num >= 10:
    print("10보다 크거나 같습니다.")
elif 5 <= num < 10:
    print("5보다 크거나 같지만 10보다 작습니다")
else:
    print("5보다 작습니다")

score = 81
if score >= 90:
    print("성적 A")
elif score >= 80:
    print("성적 B")
elif score >= 70:
    print("성적 C")
elif score >= 60:
    print("성적 D")
else:
    print("성적 F")

# 조건식을 조합하는 논리 연산자
num = 7
if num >= 10:
    print("10보다 크거나 같습니다.")
elif 5 <= num and num < 10:
    print("5보다 크거나 같지만 10보다 작습니다")
else:
    print("5보다 작습니다")