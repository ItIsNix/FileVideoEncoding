import gzip, lzma, base64
import string, color66
import cv2, numpy as np
from tqdm import tqdm

base64_chars = list(string.ascii_lowercase) + list(string.ascii_uppercase) + list(string.digits) + list("+/=")

def map_to_list(string: str, list_: list) -> list:
    """
    Maps a string to the indexes of characters in a list.
    :param string: a non_empty string
    :param list_: a non-empty list
    :return: a list of integers
    """

    if not set(string).issubset(set(list_)):
        raise IndexError(f'Argument <string> must be in range of list.')

    index_map = {char: i + 1 for i, char in enumerate(list_)}
    result = [index_map[char] for char in string]

    return result

def vid_encode(data: bytes) -> list[tuple[int, int, int]]:
    """
    Encodes byte data into a video-string format.
    :param data: byte data
    :return: a list of tuples
    """

    if not isinstance(data, bytes):
        raise TypeError(f'Argument <data> must be bytes; {type(data)} is invalid.')

    mult = 3
    lzma_compressed = lzma.compress(data)
    zlib_compressed = gzip.compress(lzma_compressed)
    b64_encoded = base64.b64encode(zlib_compressed).decode()
    list_mapped = map_to_list(b64_encoded, base64_chars)
    color66_mapped = list(map(color66.int_to_rgb66, list_mapped))
    color_mapped = [(r * mult, g * mult, b * mult) for r, g, b in color66_mapped]

    return color_mapped

def create_frame(color_map: list[tuple[int, int, int]], size: tuple[int, int] = (160, 90), index: int = 0) -> np.ndarray:

    width, height = size
    frame = np.zeros((height, width, 3), dtype=np.uint8)
    map_length = len(color_map)
    current_index = index

    for y in range(height):
        for x in range(width):

            if current_index >= map_length:
                break
            rgb_value = color_map[current_index]
            bgr_value = rgb_value[2], rgb_value[1], rgb_value[0]
            frame[y, x] = bgr_value
            current_index += 1
        if current_index >= map_length:
            break

    return frame, current_index


def create_video(color_map: list[tuple[int, int, int]], output_file: str, fps: int = 30, size: tuple[int, int] = (160, 90)):

    width, height = size
    fourcc = cv2.VideoWriter_fourcc(*'FFV1')
    out = cv2.VideoWriter(output_file, fourcc, fps, size)
    index = 0
    total_pixels = width * height
    total_frames = (len(color_map) + total_pixels - 1) // total_pixels

    with tqdm(total=total_frames, desc="Creating Video", unit="frame") as pbar:
        while index < len(color_map):
            frame, index = create_frame(color_map, size, index)
            out.write(frame)
            pbar.update(1)

    out.release()
