import random

# Question 1
def sum3():
    input = raw_input("Enter three numbers here: ")
    arr = [int(x) for x in input.split()]
    sum3 = 0
    for i in range(0, 3):
        sum3 += arr[i]
    print sum3

# Question 2
def got6():
    input = raw_input("Enter a series of number: ")
    arr = [int(x) for x in input.split()]
    got6 = False
    if arr[0] == 6 or arr[len(arr)-1] == 6:
            got6 = True
    print got6

# Question 3
def even():
    even = 0
    for i in range(0, 101, 2):
        print even + i

# Question 4
def linear_search():
    # arr = []
    arr = random.sample(range(1000), 100)
    # for x in range(100):
    #     arr.append(map(int, random.sample(range(1000),1)))
    print arr
    input1 = input("Enter a number: ")
    for x in range(0, len(arr)):
        if input1 == arr[x]:
            print(x+1)
    return "Number not in the array"

# Question 5
def fibonacci_recursion(n):
    if n <= 1:
        return n
    return fibonacci_recursion(n-1) + fibonacci_recursion(n-2)

def fibonacci_iterative(n):
    if n <= 1:
        return n
    fib = 1
    prev_fib = 1
    for x in range(1, n):
        temp = fib
        fib += prev_fib
        prev_fib = temp
    return temp

# Question 6
def rotate_left_3():
    input = raw_input("Enter numbers: ")
    arr = [int(x) for x in input.split()]
    temp = arr[0]
    for x in range(0, len(arr)-1):
        arr[x] = arr[x+1]
    arr[len(arr)-1] = temp
    print arr































# sum3()
# got6()
# even()
# linear_search()
# print fibonacci_recursion(10)
# print fibonacci_iterative(10)
# rotate_left_3()