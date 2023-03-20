# 인코딩 / 예외 처리 1

# 문자열을 바이트열로 바꿔보기
print("test".encode())
print("파이썬".encode())

# 텍스트 파일 처리
#f = open(filename, encoding="utf-8")

# 예외 처리
try:
    fname = "c:\\temp\\a.ini"
    f = open(fname)
except:   # 모든 오류에 대해서 처리
    print("Could not open " + fname)