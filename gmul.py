# metode slide
def gmul(a, b):
    p = 0
    while b:
        if b & 1:
            p ^= a
        a <<= 1
        if a & 0x100:
            a ^= 0x11B
        b >>= 1

    return p

g = 0x11B

current = g
wanted = 0x6B
power = 1

while current != wanted and (power < 10):
    print(f"current power: {power}")
    current = gmul(current, g)
    print(f"result: {hex(current)}")
    power += 1


