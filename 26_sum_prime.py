def is_prime (n):
    if n < 2:
        return False
    else:
        for i in range (2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
            
        return True
def sum_primes (n):
    sum = 0
    for i in range (n):
        if is_prime(i):
            sum = sum + i
    return sum

print(sum_primes(10))
