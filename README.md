# Movie Clip

## Usage

### Prerequisites

This script is powered by `moviepy`

```shell
pip install moviepy
# or
pip3 install moviepy
```

[Installation reference](https://ithelp.ithome.com.tw/articles/10230356)

### Step 1: Change source file

>This file need to be put in the same dir of src file
>The source file must be `.mp4`.

Then change `line 27` to:

```python
src_file = <your mp4>
```

### Step 2: Execute

```python
$python ./clip.py
```

After executing, you will see the info following:

```shell
[+] Current path:  D:\video\conan_2
[+] Start Video Cut

Enter start time/end time(s):
```

Then enter the timestamp you want to clip in following format:

```shell
<start_min>.<start_sec> <end.min>.<end.sec>
```

For example:

```shell
Enter start time/end time(s): 26.21 26.23
```

### Step 3: Check output file

Output files will be in the `clip<Number>.mp4` format

The number will be **auto-generated** by script by reading the highest number in your dir.

You only need to check **whether the duration is correct**

## Reference

http://lausai360.blogspot.com/2017/04/python.html

https://github.com/Zulko/moviepy

https://zulko.github.io/moviepy/ref/VideoClip/VideoClip.html#moviepy.video.io.VideoFileClip.VideoFileClip
