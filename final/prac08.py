# 1 2
f = open("convert.ini")
list1 = f.readlines()
for line in list1:
    line = line[:-1]
    print(line)
f.close()

# 3
f = open("convert.ini")
folder = f.readline()
folder = folder[:-1]
print(folder)
file1 = f.readline()
file1 = file1[:-1]
print(file1)
file2 = f.readline()
file2 = file2[:-1]
print(file2)
f.close()

# 주어진 폴더에서 전체 파일 목록 만들기
import os
fileList = os.listdir(folder)
#print(fileList)

# 전체 파일 목록에서 "jpg"로 끝나는 파일 이름 찾기 
for filename in fileList:
    if filename.endswith("." + file1):
        print(filename)

# 4
from PIL import Image
def convert(openFileName, saveFileName):
    m = Image.open(openFileName)
    m.save(saveFileName)
    
f = open("convert.ini")
folder = f.readline()
folder = folder[:-1]
print(folder)
file1 = f.readline()
file1 = file1[:-1]
print(file1)
file2 = f.readline()
file2 = file2[:-1]
print(file2)
f.close()

# 주어진 폴더에서 전체 파일 목록 만들기
import os
fileList = os.listdir(folder)
#print(fileList)

# 전체 파일 목록에서 "jpg"로 끝나는 파일 이름 찾기 
for filename in fileList:
    if filename.endswith("." + file1):
        #print(filename)
        s = folder  + "\\" + filename
        d = folder  + "\\" + filename[:-len(file1)] + file2
        print(s + " ==> " + d)
        convert(s, d)