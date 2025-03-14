# Hide your homework files
A very silly program that encodes and decodes any file in a silly video format

### Libraries to install:
```pip install tqdm opencv-python lzma```

---
### Usage
You can run `py -I main.py` then run `encode_file(*<FILE_PATH>*, *<OUTPUT_PATH> (optional)*, *<width> (optional)*, *<height> (optional)*, *<fps> (optional)*)` to encode a file, the default arguments for width, height and fps are 160, 90 and 30 respectively.
Or you can use `decode_file(*<VIDEO_PATH>*)` to decode an encoded video.

You can also do `test(*<FILE_PATH>*)` to encode and decode a file at the same time.. but I don't know why that exists.
***
### Note
It may take a long time for the file to be prepared if it's of a bigger size.

This is how the video will look like, a garbled mess of pixels, which is good!
![image](https://github.com/user-attachments/assets/0a7164f7-168c-40e2-970d-84d54ab6eb69)
