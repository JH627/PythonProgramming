# 자료구조 1 리스트, 튜플

### 리스트
e = []   # empty list
l1 = [1, 2, 3, "abc"] # 요소가 4개인 리스트
l2 = [1, 2, 3, [1, 2]] # 요소에 리스트가 포함됨

# 리스트의 요소 개수 확인
len([])   # 0
len(e)
len(l1)
len(l2)
len([1, 2, 3, "abc"])
len([1, 2, 3, [1, 2]])

# 인덱싱
l = [1, 2, 3, "abc"] # 리스트 생성 
print(l[0], l[1], l[2], l[3]) # 순서대로 출력
print(l[-1], l[-2], l[-3], l[-4]) # 거꾸로 출력

# 슬라이싱
a = [1, 2, 3, "abc"] 
print(a[1:3])

# 확장 슬라이싱
a = [1, 2, 3, "abc", 4, 5]
a[2:5:2]    # [시작인덱스:끝인덱스:스텝] [3, 4] 

# 연결하기
a = [1, 2, 3]
b = ["abc", 4, 5]
c = a + b # 두 개의 리스트를 붙여서 c에 저장
print(c)

# 반복하기
a = [1, 2]
b = a * 4
print(b)      # [1, 2, 1, 2, 1, 2, 1, 2]

# 리스트 요소 수정
a = [1, 2, 3, "abc"] 
a[2] = 4     # [1, 2, 4, "abc"]
a[3] = ["ab", 'a', "def"] # [1,2,3,["ab",'a',"def"]]

# 리스트이름[시작인덱스:끝인덱스] = 새로운 값
a = [1, 2, 3, "abc"] 
a[1:2] = ['g', 'h'] # [1, 'g', 'h', 3, "abc"]
a[2:4] = ["ab", 'a', "def"]   # [1, 'g', "ab", 'a', "def", "abc"]

# 리스트 요소 삭제
a = [1, 2, 3, "abc", 'g', 'h'] 
del a[1] # a[1:2] = [], [1, 3, "abc", 'g', 'h']

# 리스트 요소 범위 삭제
a = [1, 2, 3, "abc", 'g', 'h'] 
a[1:2] = [] # [1, 3, "abc", 'g', 'h']
a[2:4] = [] # [1, 3, 'h']
del(a[0:2]) # ['h']

# 리스트 요소 제거
a = [1, 3, 5, 7, 9, 7, 5, 3, 1]
a.remove(5)   # [1, 3, 7, 9, 7, 5, 3, 1]
a.remove(3)   # [1, 7, 9, 7, 5, 3, 1]
a.remove(3)   # [1, 7, 9, 7, 5, 1]

# 리스트에 포함된 요소 x의 개수 세기
a = [1, 5, 7, 5, 7, 5, 3, 1]
a.count(5)            # 3
a.count(3)            # 1
a.count(7)            # 2

# 요소의 존재여부 확인
a = [4, 8, 7, 2, 1] 
8 in a         # True
9 in a         # False

# 인덱스 확인하기
a = [4, 8, 7, 2, 1] 
a.index(8)         # 1
a.index(1)         # 4

# 리스트 요소 추가
a = [1, 2, 3] 
a.append(4)       # [1, 2, 3, 4]
a.append('5')     # [1, 2, 3, 4, '5']
a.append([2, 3])  # [1, 2, 3, 4, '5', [2, 3]] 

# 리스트 요소 삽입
a = [4, 8, 7, 2, 1] 
a.insert(2, 5)  # [4, 8, 5, 7, 2, 1]
a.insert(1, [1, 6])  # [4, [1, 6], 8, 5, 7, 2, 1]

# 리스트 요소 정렬
a = [4, 8, 7, 2, 1] 
a.sort()      # [1, 2, 4, 7, 8]

b = ['g', 'o', 'o', 'd']
b.sort()      # ['d', 'g', 'o', 'o']

# 리스트 요소 뒤집기
a = [4, 8, 7, 2, 1] 
a.reverse()           # [1, 2, 7, 8, 4]

# for문으로 리스트 접근
a = [4, 8, 7, 2, 1] 
for n in a:
    print(n)
l = [1, 'g', 'h', 3, "abc"]
for n in l:
    print(n)

### 튜플 (변경 불가)
tuple1 = (2,)       # 튜플 생성
tuple2 = 2,         # 튜플 생성
tuple3 = ("hello",) # 튜플
tuple4 = "hello",   # 튜플
tuple5 = (2)        # 정수
tuple6 = ("hello")  # 문자열

# 튜플의 요소 개수 확인
e = ()
t1 = (1, 2, 3, "abc")
t2 = (1, 2, 3, (1, 2)) 
t3 = 1, 2, 3, [1, 2], (1, 2)
len(())   # 0
len(e)
len(t1)
len(t2)

# 인덱싱
a = (1, 2, 3, "abc") # 튜플 생성 
print(a[0], a[1], a[2], a[3]) # 순서대로 출력
print(a[-1], a[-2], a[-3], a[-4]) # 거꾸로 출력

# 슬라이싱
t1 = (1, 2, 3, "abc") 
t2 = t1[1:3]
print(t2)

# 확장 슬라이싱 [시작인덱스:끝인덱스:스텝]
a = (1, 2, 3, "abc", 4, 5)
a[2:5:2]    # (3, 4)
a[2:6:2]    # (3, 4)

# 연결하기
t1 = (1, 2, 3)
t2 = ("abc", 4, 5)
t = t1 + t2
print(t)  # (1, 2, 3, "abc", 4, 5)

# 반복하기
a = (1, 2)
b = a * 4
print(b)      # (1, 2, 1, 2, 1, 2, 1, 2)

# 리스트를 튜플로 변환
list1 = [1, 2]
tuple1 = tuple(list1)
tuple2 = tuple([1, 2, 3])

# 튜플을 리스트로 변환
tuple1 = (1, 2)
list1 = list(tuple1)
list2 = list((1, 2, 3))

# 함수에서 여러 값을 함께 반환
def funcReturnsTuple():
    return 1, 2

def funcReturnsList():
    return [3, 4, 5]

tuple1 = funcReturnsTuple()
list1 = funcReturnsList()
x, y = funcReturnsTuple()
a, b, c = funcReturnsList()

# 튜플 버전
def orderNumbers(num1, num2):
    if num1 <= num2:
        return num1, num2
    else:
        return num2, num1

# 리스트 버전
def orderNumbers(num1, num2):
    if num1 <= num2:
        return [num1, num2]
    else:
        return [num2, num1]