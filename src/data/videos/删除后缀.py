import os

for name in os.listdir("."):
    if name.split(".")[-1] !="mp4" and name.split(".")[-1]!="webm":
        continue
    print(name)
    newname=name.split(".")[0]
    os.renames(name,newname)