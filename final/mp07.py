list1 = []

while True:
    geo = input("입력하세요")
    if geo == "":
        break
    else:
        list1.append(geo.split(",")) 
    
country = input("검색할 도시나 국가를 입력하세요: ")
print(country,"을(/를) 검색합니다")
for i in range(0,len(list1)):
    if list1[i][2]== country:
        print (list1[i])
    if list1[i][3]== country:
        print (list1[i])

f = open("GeoCoords.txt",'a')
f.write(country)
f.close()


