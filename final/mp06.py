import math

def square(i):
    a=[]
    a.append(int(input("x1 좌표를 입력하세요: ")))
    a.append(int(input("y1 좌표를 입력하세요: ")))
    a.append(int(input("x2 좌표를 입력하세요: ")))
    a.append(int(input("y2 좌표를 입력하세요: ")))
    list1[i] = tuple(a)
    
def triangle(i):
    a=[]
    a.append(int(input("x1 좌표를 입력하세요: ")))
    a.append(int(input("y1 좌표를 입력하세요: ")))
    a.append(int(input("x2 좌표를 입력하세요: ")))
    a.append(int(input("y2 좌표를 입력하세요: ")))
    a.append(int(input("x3 좌표를 입력하세요: ")))
    a.append(int(input("y3 좌표를 입력하세요: ")))
    list1[i] = tuple(a)

def circle(i):
    a=[]
    a.append(int(input("x 좌표를 입력하세요: ")))
    a.append(int(input("y 좌표를 입력하세요: ")))
    a.append(int(input("r을 입력하세요: ")))
    list1[i] = tuple(a)

def figure(i):
    if list1[i] == '사각형':
        square(i+1)
    elif list1[i] == '삼각형':
        triangle(i+1)
    else:
        circle(i+1)
      
list1 = ["a", 1, "b", 2, "c", 3, "d", 4 , "e", 5 ]

for i in range(0,len(list1),2):
    list1[i]=input("도형을 입력하세요: ")
    figure(i)

for i in range(0,len(list1),2):
    if list1[i] == '사각형':
        a= (list1[i+1][2] - list1[i+1][0]) * (list1[i+1][1] - list1[i+1][3])
        print(list1[i],"의 면적:", a)
        b= 2 * (list1[i+1][2] - list1[i+1][0]) + 2 * (list1[i+1][1] - list1[i+1][3])
        print(list1[i],"의 둘레:", b)
    elif list1[i] == '삼각형':
        a= 0.5 * (list1[i+1][4] - list1[i+1][2]) * (list1[i+1][1] - list1[i+1][5])
        print(list1[i],"의 면적:", a)
        b= (list1[i+1][4] - list1[i+1][2]) + (list1[i+1][1] - list1[i+1][5]) + (math.sqrt(((list1[i+1][2] - list1[i+1][0]) ** 2) + ((list1[i+1][3] - list1[i+1][1]) ** 2)))
        print(list1[i],"의 둘레:", b)       
    else:
        a= math.pi * (list1[i+1][2] ** 2)
        print(list1[i],"의 면적:", a)
        b= 2* math.pi * list1[i+1][2]
        print(list1[i],"의 둘레:", b)
