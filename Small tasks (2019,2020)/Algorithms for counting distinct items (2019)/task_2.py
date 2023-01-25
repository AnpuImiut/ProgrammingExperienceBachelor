import random
import math
import time

def generate_random_hash(n):
    hash_function = list()
    for i in range(0, n):
        while True:
            random_number = random.random()
            if random_number not in hash_function:
                hash_function.append(random_number)
                break
    return hash_function

def generate_random_input(m, n):
    return [random.randint(1,n) for i in range(m)]

def exact_solution(input_stream):
    return len(set(input_stream))

def fm(input_stream, n):
    random_hash = generate_random_hash(n)
    h_min = 1
    for i in range(0, len(input_stream)):
        hash_value = random_hash[input_stream[i] - 1]
        if hash_value < h_min:
            h_min = hash_value
    return 1/h_min

#solution by bitshifting and testing
def right_most_bit(z, d):
    mask = 1
    for i in range(0, d):
        if z & mask != 0:
            return i
        else:
            mask = mask << 1
    return d

def ams(input_stream, n):
    d = math.ceil(math.log(n, 2))
    field_max = math.pow(2, d)
    a = random.randint(0, field_max - 1)
    b = random.randint(0, field_max - 1)
    R = 0

    for i in range(0, len(input_stream)):
        z = int((a*input_stream[i] + b) % field_max)
        r = right_most_bit(z, d)
        R = max(R, r)
    return math.pow(2, R)

#as accuracy measurement we choosed the ratio
def accuracy(true_val,estimation):
    return estimation/true_val

random.seed()
n,m = input("Pls enter n and m:").split()
n = int(n)
m = int(m)
iterations = int(input("Pls enter the amount of iterations:"))
ratio1=ratio2 = 0
time_av1=time_av2=0
view = bool(int(input("simple view(0) or extended view(1):")))
for i in range(0, iterations):
    random_input = generate_random_input(m, n)
    number_of_items = exact_solution(random_input)
    if(view):
        print( "number of items:" , number_of_items)
    time1 = time.time_ns()
    approximation1 = fm(random_input, n)
    ratio1 += accuracy(number_of_items,approximation1)
    time2 = time.time_ns()
    time_av1=time2 - time1
    if (view):
        print( "approximation of Flajolet-Martin algorithm:" , accuracy(number_of_items,approximation1))
        print("Time in nano_sec: " ,time2 - time1)
    time3 = time.time_ns()
    approximation2 = ams(random_input, n)
    ratio2 += accuracy(number_of_items,approximation2)
    time4 = time.time_ns()
    time_av2=time4 - time3
    if (view):
        print( "approximation of AMS-Sketch algorithm:" , accuracy(number_of_items,approximation2))
        print("Time in nano_sec: " ,time4 - time3)
print("")
print("average ratio for Flajolet-Martin algorithm:",ratio1/iterations)
print("average time for Flajolet-Martin algorithm(nano_sec):", time_av1/iterations)
print("average ratio for AMS-Sketch algorithm:",ratio2/iterations)
print("average time for AMS-Sketch algorithm(nano_sec):",time_av2/iterations)

