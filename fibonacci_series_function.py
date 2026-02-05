# Problem: Generate the first n numbers of the Fibonacci sequence.
# Approach: Iteratively update two variables to compute Fibonacci numbers and append them to a list.
def fibonacci(n):
    if n <= 0:
        raise ValueError("n must be positive")
    a, b = 0, 1
    fib_series = []
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series
num = int(input("Enter a number: "))
print(fibonacci(num))
