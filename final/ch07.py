# 파일 입출력
f = open("t.txt") # 열기, f = open("t.txt", "r")
s = f.read()	  # 파일 내용 전체 읽기
print(s)          # 읽은 내용 출력
f.close()         # 파일 닫기

f = open("t.txt", "w")
f.write("hello world")
f.close()

# 텍스트 파일 읽기
f = open("t.txt") # f = open("t.txt", "r")
for line in f:
    print(line, end = '') # line에는 이미 줄바꿈 문자가 들어있음
f.close()         # 파일 닫기

# readline() 함수
f = open("t.txt")   # f = open("t.txt", "r")
line = f.readline() # 한 줄 읽어옴
while line:         # 파일의 끝에 도달하면 False
    print(line, end = '')
    line = f.readline()
f.close()           # 파일 닫기

# readlines() 파일 전체를 읽어서 리스트에 저장
f = open("t.txt") # f = open("t.txt", 'r')
# 파일 전체의 내용을 리스트로 만듦
lines = f.readlines() 
for line in lines:
    print(line, end = '')
f.close()         # 파일 닫기

# with 문
with open("t.txt") as f:
    for line in f:
        print(line, end = '')

# 디렉토리의 파일 목록 뽑기
import os		# os모듈을 사용하기 위해 필요함
path = "C:/temp" 	# 윈도우에서도 "/" 활용 가능
#path = "C:\\temp" 	# 백슬래쉬는 두 번 써야 함
filelist = os.listdir(path)	# 파일 목록을 리스트로 구성
