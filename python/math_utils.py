# math_utils.py - Statistical utility functions
def mean(numbers):
return sum(numbers) / len(numbers)

def maximum(numbers): return max(numbers)

def minimum(numbers): return min(numbers)

def range_of(numbers):
return max(numbers) - min(numbers)
=======
# python/math_utils.py - Mathematical and statistical utility functions

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def is_even(n):
    return n % 2 == 0

def factorial(n):
    if n < 0:
        raise ValueError(f"factorial() not defined for negative values, got {n}")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def mean(numbers):
    if not numbers:
        raise ValueError("mean() requires a non-empty list.")
    return sum(numbers) / len(numbers)

def maximum(numbers):
    return max(numbers)

def minimum(numbers):
    return min(numbers)

def range_of(numbers):
    return max(numbers) - min(numbers)
