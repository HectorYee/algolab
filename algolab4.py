# Question 1

def linear_congruential(num):
    r = 123456789
    a = 101427
    b = 321
    m = (2**32)

    counter = 0

    while counter < num:
        r = (a * r + b) % m
        counter += 1
        print (r)

