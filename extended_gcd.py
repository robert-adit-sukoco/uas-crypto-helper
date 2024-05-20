from galois import GF

field = GF(991)

# return d,x,y such that d = gcd(a,b) and d = ax + by
def egcd(a, b):
    x2, x1, y2, y1 = 1, 0, 0, 1
    print(f"- | - | - | {a} | {b} | {y2} | {y1}")
    while b > 0:
        q, r = a // b, a % b
        x, y = x2 - q * x1, y2 - q * y1
        a, b, x2, x1, y2, y1 = b, r, x1, x, y1, y
        print(f"{q} | {r} | {y} | {a} | {b} | {y2} | {y1}")

    return (a, x2, y2)



print(egcd(71, field))
