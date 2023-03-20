f1 = open("MP08Data1.txt")
f2 = open("MP08Data2.txt")
l1 = f1.readlines()
l2 = f2.readlines()
f1.close()
f2.close()

# 줄바꿈 문자 제거
for i in range(len(l1)):
    l1[i] = l1[i][:-1]
for i in range(len(l2)):
    l2[i] = l2[i][:-1]
   
i1 = 0
i2 = 0
while i1 < len(l1) and i2 < len(l2):
    if float(l1[i1]) >= float(l2[i2]):
        print(l1[i1])#, end='')
        i1 += 1
    else:
        print(l2[i2])#, end='')
        i2 += 1
# 남은 리스트 처리 
if i1 < len(l1):
    for i in range(i1, len(l1)):
        print(l1[i])#, end='')
if i2 < len(l2):
    for i in range(i2, len(l2)):
        print(l2[i])#, end='')
