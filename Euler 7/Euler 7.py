import time
import math

def is_prime(num):
    if num%2 == 0:
        return False
    for i in range(3,int(math.sqrt(num)+1)):
        if num%i == 0:
            return False
    return True

def find_prime(target_prime = 6):
    count = 0
    # for i in range(1,(target_prime)):
    it=0
    while count<target_prime:
        it+=1
        if is_prime(it):
            count+=1
        if count == target_prime:
            return it

time1 = time.time()
print(find_prime(10001))  
print("time elapsed:",(time.time()-time1))