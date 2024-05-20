def gcd(a : int, b : int):
    if b == 0:
        return a
    new_a = b
    new_b = a % b
    return gcd(new_a, new_b)

def euler_totient(n : int):
    N = 1
    for i in range(2,n):
        if gcd(n, i) == 1:
            N += 1
    return N



if __name__ == "__main__":
    print(euler_totient(16))
