# 자료형
print(type("안녕하세요"))
print(type(2))

str3 = '''test
    test2
    test3'''
print(str3)

# 이스케이프 시퀀스
print("안녕하세요.\t첫 번째 파이썬 프로그램\n")
print("백슬래시를 표현하려면 \\를 써야 합니다.")
print("문자열 상수에서 큰 따옴표 \" 표현 방법")
print('문자열 상수에서 큰 따옴표 " 표현 방법')
print('문자열 상수에서 작은 따옴표 \' 표현 방법')
print("문자열 상수에서 작은 따옴표 ' 표현 방법")

# 산술 연산 순서 (연산자 우선 순위)
print(((2 + 3) * 4) ** 2)

# 변수 생성
a = 5         # a라는 이름의 변수 생성
print(a)
b = "hello"   # b라는 이름의 변수 생성
print(b)
a = "hello2"
print(a)
c = a # c를 생성하고 a 이름표 공간에 붙임
print(c)

# 복합 연산자
a = 5 
a += 2  # 변수 = 변수 + 값
a -= 2.1 # 변수 = 변수 - 값
a *= 2.1 # 변수 = 변수 * 값
a /= 2.1 # 변수 = 변수 / 값
print(a)
a = 5 
a //= 2 # 변수 = 변수 + 값
a %= 2 # 변수 = 변수 % 값
a **= 2 # 변수 = 변수 ** 값
print(a)

# 문자열과 덧셈 연산자
str1 = "첫 번째 "
str2 = "문자열 연결"
newstr = str1 + str2
print(newstr)

newstr = str1 + "로" + str2 + "합니다"
print(newstr)

print("첫 번째 " + "문자열 연결")

# 분리해서 출력하기
print(1, "첫 번째 항목")
print(1, "과일", "사과, 배, 수박")

# 공백 문자 대신 다른 것으로 분리해서 출력하기
print("첫 번째", "문자열 연결", sep = "로 ")
print(2, 3, sep = ", ")

# 줄바꿈 문자 바꿔서 출력하기
print("첫 번째", "문자열 연결", end = "입니다")
print(2, 3, end = " ")
print(2, 3, end = "\n") # default

# 입력받기
ch = input("글자 한 개를 입력하세요: ")
num = input("1~100 사이의 정수 한 개를 입력하세요: ")
print(ch)
print(num)

# 문자열을 숫자로 변환
num = input("정수 한 개를 입력하세요: ")
print(num)
intNum = int(num)
print(intNum)
floatNum = float(num)
print(floatNum)

# 숫자를 문자열로 변환
str1 = str(2.3)
str2 = str(3)
str3 = str(2.3e10)
str4 = str(2.3e-10)
print(str1)
print(str2)
print(str3)
print(str4)