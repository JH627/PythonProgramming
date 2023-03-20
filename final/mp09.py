import json
import os
from PIL import Image
f=open("MP09.json")
d = json.load(f)
f.close()

path1=d[0]["Path"]
path2=d[1]["Path"]
path3=d[2]["Path"]

src1=d[0]["Src"]
src2=d[1]["Src"]
src3=d[2]["Src"]

dest1=d[0]["Dest"]
dest2=d[1]["Dest"]
dest3=d[2]["Dest"]

fileList1 = os.listdir(path1)
for filename in fileList1:
    if filename.endswith("." + src1):
        s = path1  + "\\" + filename
        d = path1  + "\\" + filename[:-len(src1)] + dest1
        print(s,d)
        m = Image.open(s)
        m.save(d)
        
fileList2 = os.listdir(path2)
for filename in fileList2:
    if filename.endswith("." + src2):
        s = path2  + "\\" + filename
        d = path2  + "\\" + filename[:-len(src2)] + dest2
        print(s,d)
        m = Image.open(s)
        m.save(d)

fileList3 = os.listdir(path3)
for filename in fileList3:
    if filename.endswith("." + src3):
        s = path3  + "\\" + filename
        d = path3  + "\\" + filename[:-len(src3)] + dest3
        print(s,d)
        m = Image.open(s)
        m.save(d)
