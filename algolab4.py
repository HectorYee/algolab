import random
import time

millis = int(round(time.time() * 1000))
print (millis)

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

# Question 2

class Random:
    seed = 0

    def __init__(self, seed = None):
        if seed is None:
            seed = millis
        else:
            self.seed = seed
        print(seed)




    def setSeed(self, long_seed):
        self.seed = long_seed

    # def next_boolean(self):

    def next_float(self):
        self.next_double()

    def next_double(self):
        random_no = self.seed * random
        print(random_no)






def main():
    ran = Random()
    ran2 = Random(12)
    ran3 = ran.next_double()




if __name__ == "__main__":
    main()