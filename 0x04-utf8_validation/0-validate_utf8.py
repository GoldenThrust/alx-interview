#!/usr/bin/python3
""" UTF-8 Validator """


def validUTF8(data):    
    """
    Check if a given list of integers represents a valid UTF-8 encoding.

    Args:
    - data (list of int): A list of integers where each integer represents 1 byte of data.

    Returns:
    - bool: True if data is a valid UTF-8 encoding, else return False.

    UTF-8 Encoding Rules:
    - A character in UTF-8 can be 1 to 4 bytes long.
    - The data set can contain multiple characters.
    - Each integer in the data list represents 1 byte of data.

    Algorithm:
    - Iterate through each byte in the data.
    - Check if the byte is a leading byte or a trailing byte based on UTF-8 rules.
    - For a leading byte:
      - Determine the number of trailing bytes expected for the current character.
      - Check if the byte follows the UTF-8 rules for leading bytes.
    - For a trailing byte:
      - Check if the byte follows the UTF-8 rules for trailing bytes.
    - Return True if the data represents a valid UTF-8 encoding, else return False.
    """

    trailing_bytes = 0

    for byte in data:
        if trailing_bytes == 0:
            # valid 0 to 127
            if byte >> 7 == 0b0:
                continue
            # valid  192 to 223
            elif byte >> 5 == 0b110:
                trailing_bytes = 1
            # valid 224 to 239
            elif byte >> 4 == 0b1110:
                trailing_bytes = 2
            # valid 238 to 247
            elif byte >> 3 == 0b11110:
                trailing_bytes = 3
            else:
                return False
        else:
            # 128 to 191
            if byte >> 6 != 0b10:
                return False
            trailing_bytes -= 1

    return trailing_bytes == 0
