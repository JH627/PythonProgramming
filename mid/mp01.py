tem = float(input("기온 입력 : "))
wind = float(input("풍속 입력 : "))
wind *= -3.6
wc = 13.12 + 0.621 * tem - 11.37 * pow(wind, 0.16) + 0.3965 * tem * pow(wind, 0.16)

print("체감 온도 : " + str(wc))