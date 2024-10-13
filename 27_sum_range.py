def is_prime (n):
    if n < 2:
        return False
    else:
        for i in range (2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
            
        return True
    
def print_primes_in_range(start, end):
    primes = []
    for i in range(start, end + 1):
        if (is_prime(i)):
            primes.append(str(i))
    print(", ".join(primes))
print_primes_in_range(10000, 10050)