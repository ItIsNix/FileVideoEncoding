import gzip, lzma, base64
import string, color66
import cv2
from tqdm import tqdm

base64_chars = list(string.ascii_lowercase) + list(string.ascii_uppercase) + list(string.digits) + list("+/=")

def map_to_list(indices: list[int], list_: list) -> str:
    """
    Maps the indexes of a list to the characters of a list.
    :param indices: a non_empty list of integers
    :param list_: a non-empty list of characters
    :return: a string
    """

    if any(index < 1 or index > len(list_) for index in indices):
        raise ValueError("Indices must be within the range of the list length.")

    result = ''.join([list_[index - 1] for index in indices])

    return result

def read_video(video_path: str) -> list[tuple[int, int, int]]:
    cap = cv2.VideoCapture(video_path)
    result = []

    with tqdm(total=int(cap.get(cv2.CAP_PROP_FRAME_COUNT)), desc="Reading Video", unit="frame") as pbar:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            result.extend(tuple(map(int, frame_rgb[y, x])) for y in range(frame_rgb.shape[0]) for x in range(frame_rgb.shape[1]))
            pbar.update(1)

        cap.release()

    result = list(t for t in result if t != (0, 0, 0))
    seperator = (255, 255, 255)
    sep_idx = result.index(seperator)
    return result[:sep_idx], result[sep_idx + 1:]

def vid_decode(data: list[tuple[int, int, int]]) -> bytes:
    """
        Decodes color data into a byte format.
        :param data: a list of tuples (color data of a video)
        :return: data in bytes
    """

    if not isinstance(data, list):
        raise TypeError(f'Argument <data> must be a list; {type(data)} is invalid.')

    mult = 3
    color_mapped = [(int(r / mult), int(g / mult), int(b / mult)) for r, g, b in data]
    int_mapped = list(map(color66.rgb66_to_int, color_mapped))
    list_mapped = map_to_list(int_mapped, base64_chars)
    b64_decoded = base64.b64decode(list_mapped)
    zlib_decompressed = gzip.decompress(b64_decoded)
    lzma_decompressed = lzma.decompress(zlib_decompressed)

    return lzma_decompressed
