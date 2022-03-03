import os

path = os.getcwd()
# print(path)
files = os.listdir(path)
# print(files)
# index=0
for file in files:
    if "新我們這一家 " in file:
        new_file = file
        new_file = new_file.replace("新我們這一家 第", "")
        new_file = new_file.replace("集", "")
        pos = new_file.find(" ")
        new_file = new_file[0:pos] + ".mp4"
        print(new_file)
        os.rename(path+"\\"+file, path+"\\"+new_file)

# files = os.listdir(path)
# print(files)