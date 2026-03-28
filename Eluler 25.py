def is_n_digits(x,n):
    if len(str(x)) > n-1:
        return True
    else:
        return False


def gen_fib_to_n_dig(n_dig):
    previous_terms = [1,1]
    current_value = 2
    next_value = 0
    index = 2
    run = True
    while run:
        index+=1
        current_value = previous_terms[0] + previous_terms[1]
        previous_terms[0], previous_terms[1] = previous_terms[1], current_value
        if is_n_digits(current_value,n_dig):
            print(index)
            run = False


gen_fib_to_n_dig(1000)

