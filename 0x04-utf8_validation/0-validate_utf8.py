#usr/bin/python3

def valid_utf8(data):
    """
    Method that determines if a given data set represents a valid
    UTF-8 encoding.
    Return: True if data is a valid UTF-8 encoding, else return False
    A character in UTF-8 can be 1 to 4 bytes long
    The data set can contain multiple characters
    The data will be represented by a list of integers
    Each integer represents 1 byte of data, therefore you only
    need to handle the 8 least significant bits of each integer
    """
    # Variable for counting number of bytes in UTF-8 Character
    num_bytes = 0

    # Masks for checking if byte is valid (Starts with 10)
    mask1 = 1 << 7
    mask2 = 1 << 6

    for i in data:

        mask_n_byte = 1 << 7

        if num_bytes == 0:
            # Count number of bytes the UTF-8 Character will have
            while mask_n_byte & i:
                num_bytes += 1
                mask_n_byte = mask_n_byte >> 1

            # If number of bytes did not increase then it has 1 byte
            # which is the same we are counting so no need to check next bytes
            # for current character
            if num_bytes == 0:
                continue

            # A character in UTF-8 can be 1 to 4 bytes long
            # But 1 byte characters start in 0 so num_bytes should never
            # be 1
            if num_bytes == 1 or num_bytes > 4:
                return False

        else:
            # Every byte that is not the first byte of a character should start
            # with 10, otherwise is not valid
            if not (i & mask1 and not (i & mask2)):
                    return False

        # If bytes of character are valid, then the count will decrease with
        # each byte until a new character starts
        num_bytes -= 1

    # All characters were verified correctly with their proper byte count
    if num_bytes == 0:
        return True

    return False
