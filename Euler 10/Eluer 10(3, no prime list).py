import time
import math

def is_prime(num):
    if num%2 == 0:
        return False
    for i in range(3,int(math.sqrt(num)+1)):
        if num%i == 0:
            return False
    return True

def sum_primes(max_val = 2000000):
    sigma = 2
    for n in range(3,(max_val),2):
        if is_prime(n):
            sigma += n 
    return sigma

time1 = time.time()
print(sum_primes(2000000))  
print("time elapsed:",(time.time()-time1))