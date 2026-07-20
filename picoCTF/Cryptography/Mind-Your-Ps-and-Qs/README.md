# picoCTF - Mind Your Ps and Qs

## Challenge Information

| Field      | Details                                   |
| ---------- | ----------------------------------------- |
| Platform   | picoCTF                                   |
| Category   | Cryptography                              |
| Difficulty | Medium                                    |
| Skills     | RSA, Mathematical Analysis, Factorization |

---

# Overview

Mind Your Ps and Qs is a cryptography challenge focused on breaking a weak RSA implementation.

The challenge demonstrates how RSA security depends on the difficulty of factoring large prime numbers. If the RSA modulus can be factored, the private key can be recovered and encrypted data can be decrypted.

The attack path includes:

* Analyzing RSA parameters
* Factoring the modulus
* Recovering the private key
* Decrypting the ciphertext

---

# Reconnaissance

The challenge provides RSA parameters:

* Public exponent (`e`)
* Modulus (`n`)
* Ciphertext (`c`)

The values were analyzed to understand the encryption setup.

RSA encryption:

```
c = m^e mod n
```

where:

* `m` is the plaintext
* `e` is the public exponent
* `n` is the modulus

---

# Cryptographic Analysis

RSA security depends on the modulus being generated from two large prime numbers:

```
n = p × q
```

The provided modulus was small enough to factor.

The factorization process recovered:

```
p
q
```

These values allowed calculation of Euler's totient:

```
φ(n) = (p-1)(q-1)
```

---

# Key Recovery

The private key exponent was calculated using:

```
d = e⁻¹ mod φ(n)
```

With the private key available, the ciphertext could be decrypted.

RSA decryption:

```
m = c^d mod n
```

---

# Solution

The RSA values were processed using a Python script to:

* Factor the modulus
* Calculate the private exponent
* Decrypt the ciphertext

Example workflow:

```python
p = factor(n)
q = n // p

phi = (p-1)*(q-1)

d = inverse(e, phi)

message = pow(c, d, n)
```

The resulting plaintext was converted back into readable text.

---

# Flag Retrieval

After decrypting the RSA ciphertext, the plaintext contained the challenge flag.

---

# Tools Used

* Python
* RSA mathematics
* Factorization tools
* Linux terminal

---

# Skills Demonstrated

## RSA Cryptography

Understanding public key encryption and key generation.

## Mathematical Analysis

Using weaknesses in cryptographic parameters to recover secrets.

## Cryptanalysis

Identifying weaknesses that allow encrypted data to be recovered.

---

# Technical Concepts

## RSA

RSA is an asymmetric encryption algorithm based on the difficulty of factoring large numbers.

A secure RSA implementation requires:

* Large prime numbers
* Proper key generation
* Secure parameter selection

## RSA Factorization Attack

If the modulus `n` can be factored into `p` and `q`, the private key can be calculated and the encrypted message can be recovered.
