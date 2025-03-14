from encode import vid_encode, create_video
from decode import vid_decode, read_video
import time, os

seperator = [(255, 255, 255)]

def encode_file(input_file: str, output_file: str = "encoded.avi") -> None:
    """
    Encodes a given data in a video format
    :param input_file: path to desired data
    :param output_file: path to output video
    """

    if not isinstance(input_file, str) or not isinstance(output_file, str):
        raise TypeError(f'Argument <{"input_file" if not isinstance(input_file, str) else "output_file"}> must be a string;'
                        f' {type(input_file) if not isinstance(input_file, str) else type(output_file)} is invalid.')

    with open(input_file, 'rb') as _: data = _.read()
    color_map = vid_encode(input_file.encode()) + seperator + vid_encode(data)
    create_video(color_map, output_file, size=(width, height))

def decode_file(video_path: str = "encoded.avi") -> None:
    """
        Decodes a given video to the original file format
        :param video_path: path to encoded video
    """

    if not isinstance(video_path, str):
        raise TypeError(f'Argument <video_path> must be a string; {type(video_path)} is invalid.')

    file_name, file_contents = read_video(video_path)
    file_name = vid_decode(file_name)
    file_contents = vid_decode(file_contents)

    if not os.path.exists('output'):
        os.makedirs('output')

    with open(f'output/{file_name.decode()}', 'wb') as file: file.write(file_contents)

def test(input_file: str) -> None:
    encode_file(input_file)
    print("encoding successful")
    time.sleep(1)
    decode_file("encoded.avi")
    print("decoding successful")


width, height = 160, 90
fps = 30

input_file = "pic.png"

test(input_file)