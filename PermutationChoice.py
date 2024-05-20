# PC1 array for DES
PC1 = [
    57, 49, 41, 33, 25, 17, 9,
    1, 58, 50, 42, 34, 26, 18,
    10, 2, 59, 51, 43, 35, 27,
    19, 11, 3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
    7, 62, 54, 46, 38, 30, 22,
    14, 6, 61, 53, 45, 37, 29,
    21, 13, 5, 28, 20, 12, 4
]

# PC2 array for DES
PC2 = [
    14, 17, 11, 24, 1, 5,
    3, 28, 15, 6, 21, 10,
    23, 19, 12, 4, 26, 8,
    16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55,
    30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53,
    46, 42, 50, 36, 29, 32
]

def hex_to_bin_fill64(hex_key):
    original = int(hex_key, 16)
    binary_form = str(bin(original)).zfill(64)
    return binary_form


def permute_with_PC1(key):
    """
    Permutes a 64-bit key using the PC1 array to produce a 56-bit result.

    Args:
    key (str): The 64-bit binary key represented as a string.

    Returns:
    str: The 56-bit result after permutation with PC1.
    """
    if len(key) != 64:
        raise ValueError("Key must be 64 bits long")

    # Apply PC1 permutation
    pc1_result = ''.join(key[i - 1] for i in PC1)

    return pc1_result


def permute_with_PC2(key):
    """
    Permutes a 56-bit key using the PC2 array to produce a 48-bit result.

    Args:
    key (str): The 56-bit binary key represented as a string.

    Returns:
    str: The 48-bit result after permutation with PC2.
    """
    if len(key) != 56:
        raise ValueError("Key must be 56 bits long")

    # Apply PC2 permutation
    pc2_result = ''.join(key[i - 1] for i in PC2)

    return pc2_result

