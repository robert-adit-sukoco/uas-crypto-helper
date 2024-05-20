
def modular_inverse(a, p):
    """
    Compute the modular inverse of a modulo p using the Extended Euclidean Algorithm.
    """
    if a == 0:
        raise ValueError('No inverse exists')
    
    lm, hm = 1, 0
    low, high = a % p, p
    
    while low > 1:
        ratio = high // low
        nm, new = hm - lm * ratio, high - low * ratio
        lm, low, hm, high = nm, new, lm, low
    
    return lm % p

def is_quadratic_residue(a, p):
    """
    Check if a is a quadratic residue modulo p using Euler's criterion.
    """
    return (((pow(a, (p - 1) // 2, p)) == 1) or (a == 0))

def find_points_on_elliptic_curve(p, a, b):
    """
    Find all points (x, y) on the elliptic curve y^2 = x^3 + ax + b over the field F_p.
    """
    points = []
    for x in range(p):
        rhs = (x**3 + a*x + b) % p  # Compute x^3 + ax + b mod p
        if is_quadratic_residue(rhs, p):  # Check if rhs is a quadratic residue
            for y in range(p):
                if (y**2 % p) == rhs:  # Check if y^2 = rhs mod p
                    points.append((x, y))
    return points


def point_addition(P, Q, a, p):
    """
    Add two points P and Q on the elliptic curve y^2 = x^3 + ax + b over the finite field F_p.
    """
    if P == Q:
        raise ValueError("Use point doubling for P == Q")
    
    if P == 'Infinity':
        return Q
    if Q == 'Infinity':
        return P
    
    x1, y1 = P
    x2, y2 = Q
    
    if x1 == x2 and (y1 != y2 or y1 == 0):
        return 'Infinity'
    
    if x1 == x2:
        # Point doubling case (not covered here as it needs a separate implementation)
        raise ValueError("Use point doubling for P == Q")
    
    # Calculate slope (lambda)
    try:
        m = (y2 - y1) * modular_inverse(x2 - x1, p) % p
    except ValueError:
        return 'Infinity'
    
    # Calculate x3 and y3
    x3 = (m**2 - x1 - x2) % p
    y3 = (m * (x1 - x3) - y1) % p
    
    return (x3, y3)

def point_doubling(P, a, p):
    """
    Perform point doubling on the elliptic curve y^2 = x^3 + ax + b over the field F_p.
    """
    x1, y1 = P

    if y1 == 0:
        # The result is the point at infinity
        return "Infinity"

    # Calculate lambda
    numerator = (3 * x1**2 + a) % p
    denominator = (2 * y1) % p
    inv_denominator = modular_inverse(denominator, p)
    lam = (numerator * inv_denominator) % p

    # Calculate x3
    x3 = (lam**2 - 2 * x1) % p

    # Calculate y3
    y3 = (lam * (x1 - x3) - y1) % p

    return (x3, y3)

def main():
    p = 13
    a = 2
    b = 5

    P = (3, 8)
    Q = (4, 8)

    addition_result = point_addition(P, Q, a, p)
    print(addition_result)

if __name__ == "__main__":
    main()
