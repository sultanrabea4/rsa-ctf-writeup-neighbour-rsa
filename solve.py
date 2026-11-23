"""
Neighbour-RSA solver: Fermat factorisation of an RSA modulus with close primes.

Usage:
    python solve.py <N> <e> <C>

Requires: pip install pycryptodome
"""
import sys
from math import isqrt

from Crypto.Util.number import inverse, long_to_bytes


def fermat_factor(n: int) -> tuple[int, int]:
    """Factor n = p*q when p and q are close, using Fermat's method."""
    a = isqrt(n)
    if a * a < n:
        a += 1
    while True:
        b2 = a * a - n
        b = isqrt(b2)
        if b * b == b2:
            p, q = a - b, a + b
            assert p * q == n
            return p, q
        a += 1


def decrypt(n: int, e: int, c: int) -> bytes:
    p, q = fermat_factor(n)
    phi = (p - 1) * (q - 1)
    d = inverse(e, phi)
    m = pow(c, d, n)
    return long_to_bytes(m)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(__doc__)
        sys.exit(1)
    N, E, C = (int(x) for x in sys.argv[1:4])
    plaintext = decrypt(N, E, C)
    print(plaintext.decode("utf-8", errors="replace"))
