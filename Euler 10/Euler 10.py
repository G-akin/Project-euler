def is_prime(num):
    if num%2 == 0:
        return False
    for i in range(3,num):
        if num%i == 0:
            return False
    return True


prime_list=[2]

def sum_primes(max = 1000000):
    sigma = 2
    for n in range(3,max,2):
        if is_prime(n):
            sigma += n 
    return sigma

print(sum_primes(max=20000))