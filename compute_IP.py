def compute_IP(plaintext):
    plaintext_list = list(bin(int(plaintext, 16))[2:].zfill(64))
    permute = ""

    IP = [58, 50, 42, 34, 26, 18, 10, 2,
        60, 52, 44, 36, 28, 20, 12, 4,
        62, 54, 46, 38, 30, 22, 14, 6,
        64, 56, 48, 40, 32, 24, 16, 8,
        57, 49, 41, 33, 25, 17, 9, 1,
        59, 51, 43, 35, 27, 19, 11, 3,
        61, 53, 45, 37, 29, 21, 13, 5,
        63, 55, 47, 39, 31, 23, 15, 7]

    for i in IP:
        permute += plaintext_list[i - 1]

    return permute


plaintext = "02468ACEECA86420"

result = compute_IP(plaintext)

print(hex(int(result, 2)))