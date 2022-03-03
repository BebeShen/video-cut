'''
    Cut out video by start_time & end_time (in `s`)
        output files would be named by `clipX.mp4` in order
    Author:         BebeShen
    Created at:     2021/10/02
'''
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import moviepy.editor as mpy
import os

# # Path setting
# while True:
#     print("[+] Current path: ", os.getcwd())
#     dir_list = os.listdir()
#     print("[+] List all dir, Select the video dir: \n")
#     for index, _dir in enumerate(dir_list):
#         print("\t" + str(index) + ". " + _dir)
#     _select = int(input("\n(Enter 0~" + str(len(dir_list)-1) + ", Enter '-1' to stay): "))
#     if _select == -1:
#         break
#     video_dir = dir_list[_select]
#     print(video_dir)
#     os.chdir(os.path.join(video_dir))

# print("[+] Current path: ", os.getcwd())

# File setting
src_file = "26C.mp4"
# src_file = input("\n[+] Enter the video name: ")

current_path =  os.path.dirname(os.path.abspath(__file__))
print("[+] Current path: ", current_path)
# clips = []
def FindMaxClip():
    allFileList = os.listdir(current_path)
    max_clip = 0
    for _file in allFileList:
        if not os.path.isdir(_file):
            # print(_file)
            if "clip" in _file and _file.endswith("mp4"):
                # print("[+] Direct Find ", _file)
                clip_number = _file.split("clip")[1]
                clip_number = int(clip_number.split(".")[0])
                if clip_number > max_clip:
                    max_clip = clip_number

    print("[+] Max # of Clip: ", max_clip)
    return max_clip
            # if "clip" in os.path.split(_file)[1]:
            #     print("Os path", os.path.split(_file)[1])

print("[+] Start Video Cut\n")
# Cut Video
while True:
    t1, t2 = input("Enter start time/end time(s): ").split()
    _st = t1.split(".")
    _et = t2.split(".")
    # if "." in t1 and "." in t2:
    #     t1 = float(t1.split(".")[0])*60.0 + float(t1.split(".")[1]) 
    #     t2 = float(t2.split(".")[0])*60.0 + float(t2.split(".")[1])
    # else:
    #     continue
    # print(t1,t2)
    max_clip = FindMaxClip()+1
    target_file = "clip" + str(max_clip) + ".mp4"
    # newclip =  mpy.VideoFileClip(src_file).subclip(t1,t2)
    # # Remove audio can small shrink file size
    if len(_st) == 3:
        st = float(_st[0])*60.0 + float(_st[1] + "." + _st[2])
    elif len(_st) == 2:
        st = float(_st[0])*60.0 + float(_st[1])
    if len(_et) == 3:
        et = float(_et[0])*60.0 + float(_et[1] + "." + _et[2])
    elif len(_et) == 2:
        et = float(_et[0])*60.0 + float(_et[1])
    print(st, et)
    newclip =  mpy.VideoFileClip(src_file, audio=False).subclip(st, et)
    newclip.write_videofile(target_file)
    # ffmpeg_extract_subclip(src_file, t1, t2, targetname=target_file)

print("\n[+] End Video Cut")