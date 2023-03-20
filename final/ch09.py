# 딕셔너리
{} # 빈 딕셔너리
{ "name" : "홍길동", "age" : 20, 
  "취미" : ["영화 감상", "게임", "독서"] }

# 키는 수정 불가능한 것들만 사용 가능
d = { 1 : 2, False : 20, (1, 2) : "튜플" }
print(d[1])
print(d[False])
print(d[(1,2)])

# 딕셔너리의 요소 개수 확인
d = {}   # empty dictionary
d1 = {'a':1, 'b':2, 'c':3 }
len({})   # 0
len(d)
len(d1)

# 요소 접근 (딕셔너리_이름[키] 사용)
d = { "name" : "홍길동", "age" : 20, "취미" : ["영화 감상", "게임", "독서"] }
print(d["name"]) # 홍길동

# 요소 접근 (get()함수 사용)
print(d.get("name")) # 홍길동

# 키가 중복되면 나중에 나오는 값으로 지정됨
d = { "name" : "홍길동", "age" : 20, "취미" : ["영화 감상", "게임", "독서"], 
      "name" : "김길동" }
print(d["name"]) # 김길동

# 단일 요소 수정
d = { 1 : 2, False : 20, (1, 2) : "튜플" }
d[1] = 3
d[False] = "불린 값"
d[(1, 2)] = [1, 2]
d["key"] = "value"   # 새로운 키와 값 추가
print(d[1])
print(d[False])
print(d[(1,2)])
print(d["key"])

# 요소 값 추가 또는 수정 (update() 함수 사용)
d = { 1 : 2, False : 20, (1, 2) : "튜플" }
d.update({1:3, False:"불린 값", (1,2):[1,2],
          "key":"value" })
print(d[1])
print(d[False])
print(d[(1,2)])
print(d["key"])

# for문과 함께 사용 (key 저장)
d = { 1 : 2, False : 20, (1, 2) : "튜플" }
for n in d:   # == for n in d.keys():
    print(n)

# for문과 함께 사용 (values 저장)
d = { 1 : 2, False : 20, (1, 2) : "튜플" }
for n in d.values():
    print(n)

# 키와 값 동시 저장
d = { 1 : 2, False : 20, (1, 2) : "튜플" }
for k, v in d.items():
    print(k, v)

# 키가 딕셔너리에 있는 지 확인
d = { 1 : 2, False : 20, (1, 2) : "튜플" }
if 1 in d:
    print(d[1])
else:
    print("1은 d의 키가 아닙니다")

# 삭제
d = { 1 : 2, False : 20, (1, 2) : "튜플" }
del(d[1])
print(d) # { False : 20, (1, 2) : "튜플" }

# 전체 삭제
d = { 1 : 2, False : 20, (1, 2) : "튜플" }
d.clear()
print(d) # {}