# Movie Clip

## Description

當初因為有剪輯影片的需求，但是覺得只是要剪一些短片段，用剪輯軟體太慢又很吃電腦效能，所以直接寫scirpt來剪，只要輸入想要片段的**起始時間**和**結束時間**即可，可以精確到小數點後兩位。

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

**Example**

```shell
Enter start time/end time(s): 26.21 26.23
```

### Step 3: Check output file

Output files will be in the `clip<Number>.mp4` format

The number will be **auto-generated** by script by reading the highest number in your dir.

You only need to check **whether the duration is correct**

## Reference

* [用 python 剪輯影片 lausai](http://lausai360.blogspot.com/2017/04/python.html)

* [moviepy](https://github.com/Zulko/moviepy)

* [MoviePy Document](https://zulko.github.io/moviepy/index.html)
