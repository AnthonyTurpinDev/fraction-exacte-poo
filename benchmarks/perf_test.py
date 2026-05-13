import time
from fraction.fraction import Fraction

def benchmark_operations(n=100000):
    start = time.time()
    a = Fraction(1, 2)
    b = Fraction(1, 3)
    for _ in range(n):
        _ = a + b
        _ = a * b
        _ = a / b
    end = time.time()
    print(f"{n} opérations en {end - start:.4f} secondes")

if __name__ == "__main__":
    benchmark_operations()