# CTF Write-up: Neighbour-RSA (Equilibrium CTF 2025)

Write-up of the **Neighbour-RSA** cryptography challenge (**436 points**, medium–hard) from **Equilibrium CTF (EQCTF) 2025**. I solved it with team **PacketPirates** (3 members) as part of a Practical CTF Strategies module.

---

## Challenge
- **Category:** Cryptography (RSA)
- **Given:** modulus `N`, public exponent `e = 65537` and ciphertext `C`
- **Hint:** `q` is the prime that comes **5,000 primes after** `p`, so the two factors are relatively close

## Vulnerability
RSA is only secure if `N = p·q` is hard to factor. When `p` and `q` are **close together**, **Fermat's factorisation** recovers them quickly:

```
N = a² − b²  =  (a − b)(a + b)   →   p = a − b,  q = a + b
```
Start with `a = ⌈√N⌉` and increase `a` until `a² − N` is a perfect square.

## Solution
1. **Factor N** with Fermat's method → `p`, `q`
2. **Compute the totient:** `φ(N) = (p − 1)(q − 1)`
3. **Private key:** `d = e⁻¹ mod φ(N)`
4. **Decrypt:** `M = C^d mod N`, then convert to bytes → **flag** ✅

See [`solve.py`](solve.py) for a clean reimplementation of the approach.

## Problems Solved Along the Way
- `ModuleNotFoundError: No module named 'Crypto'` → installed **PyCryptodome** in the correct interpreter / VS Code environment
- `UnicodeDecodeError` when decoding the plaintext → decoded the bytes safely
- Heavy factoring tools (msieve, yafu) failed to install → Fermat's method made them unnecessary

## Lessons Learned
- Prime **generation patterns** can break RSA even with large key sizes
- Choosing the right algorithm (Fermat vs brute force) matters more than raw compute

## Tools
Python 3 · PyCryptodome · VS Code

## Author
**Sultan Mohammed Rabea** · [LinkedIn](https://www.linkedin.com/in/sultan-rabea/) · [GitHub](https://github.com/sultanrabea4)
