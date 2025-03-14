def int_to_rgb66(number: int) -> tuple[int, int, int]:
    """
    Maps an Integer to a 66 color tuple
    :param number: a positive integer
    :return: a tuple of 3 values (22,22,22)
    """
    if not isinstance(number, int):
        raise TypeError(f'Argument must be an integer; {type(number)} is invalid.')
    if number < 0:
        raise ValueError(f'Argument must be a positive integer; {number} is negative.')

    result: array = [0, 0, 0]
    for i in range(3):
        if number > 22:
            result[i] = 22
            number -= 22
        else:
            result[i] = number
            number = 0

    return tuple(result)

def rgb66_to_int(tuple66: tuple[int, int, int]) -> int:
    """
    Turns a 66 color tuple into an integer
    :param tuple66: a 66 color tuple
    :return: the sum of the values
    """
    if not isinstance(tuple66, tuple) or len(tuple66) != 3:
        raise TypeError(f'Argument must be a tuple of 3 integers; argument is a {type(tuple66)} of length {len(tuple66)}.')

    return sum(tuple66)

def rgb66_to_rgb256(tuple66: tuple[int, int, int]) -> tuple[int, int, int]:
    """
    Turns a 66 color tuple into a 256 color tuple
    :param tuple66: a 66 color tuple
    :return: a 256 color tuple
    """
    if not isinstance(tuple66, tuple) or len(tuple66) != 3:
        raise TypeError(f'Argument must be a tuple of 3 integers; argument is a {type(tuple66)} of length {len(tuple66)}.')

    result: array = [0, 0, 0]

    for i in range(3):
        result[i] = list(tuple66)[i] * 3

    return tuple(result)

def rgb265_to_rgb66(tuple256: tuple[int, int, int]) -> tuple[int, int, int]:
    """
    Turns a 256 color tuple into a 66 color tuple
    :param tuple256: a 256 color tuple
    :return: a 66 color tuple
    """
    if not isinstance(tuple256, tuple) or len(tuple256) != 3:
        raise TypeError(f'Argument must be a tuple of 3 integers; argument is a {type(tuple256)} of length {len(tuple256)}.')

    result: array = [0, 0, 0]

    for i in range(3):
        result[i] = int(list(tuple256)[i] / 3)

    return tuple(result)
