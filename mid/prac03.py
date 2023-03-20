#pip3 install Pillow
from PIL import Image

# 이미지 파일 열기
m = Image.open("Italy-1280.jpg")
# png 포맷으로 변환 저장
m.save("italy-1280.png")
# 이미지 보여주기
m.show()

imageName = input("확장자를 제외한 이름 입력 : ")
# 이미지 파일 열기
m = Image.open(imageName + ".jpg")
# png 포맷으로 변환 저장
m.save(imageName + ".png")
# 이미지 보여주기
m.show()
