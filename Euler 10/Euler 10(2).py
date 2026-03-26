import time

def is_prime(num):
    if num%2 == 0:
        return False
    for prime in prime_list:
        if num%prime == 0:
            return False
    return True

prime_list = [2]

def sum_primes(max = 2000000):
    sigma = 2
    for n in range(3,max,2):
        if is_prime(n):
            sigma += n 
            prime_list.append(n)
    return sigma

time1 = time.time()
print(sum_primes(max=20000))  
print("time elapsed:",(time.time()-time1))