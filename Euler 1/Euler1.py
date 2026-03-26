def num_of_mults_3_5(max_val):
    sigma = 0
    for i in range(1,max_val):
        if i%3 == 0 or i%5 == 0:
            sigma+=i

    return sigma

print(num_of_mults_3_5(1000))