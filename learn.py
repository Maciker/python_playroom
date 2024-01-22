from math import factorial

n = 5
k = 3

print(factorial(n) / (factorial(k) - factorial(n-k)))

capital = "pamplona"

print(capital.capitalize())
"""Strings are unmutable objects"""
print(capital)

capitalBytes = capital.encode('utf-8')

print(capitalBytes)

print(capitalBytes.decode('utf-8'))