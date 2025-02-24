def create_list_of_fibonacci_series(n):
    result = []
    for i in range(n):
        if i <= 1:
            result.append(i)
        else:
            result.append(result[i-1]+result[i-2])
    return result


def find_factors(n):
    factors = []
    for i in range(1, n+1):
        if n % i == 0:
            factors.append(i)
    return factors


def factorial(x):
    if x == 1:
        return 1
    return x*factorial(x-1)


def Geometric_Series(a, r, n):
    result = []
    current = a
    for i in range(n):
        result.append(current)
        current = current*r
    return result


def prime_factorization(n):
    factors = []
    Divisor = 2
    while n > 1:
        if n % Divisor == 0:
            factors.append(Divisor)
            n = n/Divisor
        else:
            Divisor += 1
    return factors


# Use Copilot to write a function which prime factorizes the factorial of
# a number. Try to improve efficiency using Copilot.
# Delete these instructions before asking Copilot for help
