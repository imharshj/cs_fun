# question 1
import time

def num_finder():
    l = []
    for i in range(2000,32001):
        if i % 7 == 0 and i % 5 != 0:
            yield i

t1 = time.clock()
#for i in num_finder():
#    print i


# Question 2
def my_factorial(n):
    if n == 1: return 1
    fact = my_factorial(n-1) * n

    return fact

# print my_factorial(10)
# x = int(raw_input())

t2 = time.clock()
print round(t2-t1)

# Question 3
def dict_writer(n):
    return {i: i*i for i in range(1,n+1)}

# print dict_writer(8)

#Question 4

def decoder(input):
    w = input.split(' ')
    words = [word for word in set(w)]
    print ' '.join(sorted(words))

decoder('hello world and practice makes perfect and hello world again')

# Question 5
def odd_squares(input):
    return [x**2 for x in input if x % 2 == 0]

print odd_squares(xrange(10))