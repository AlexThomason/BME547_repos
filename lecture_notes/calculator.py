# calculator.py
# Author: Alex Thomason

import math

def add(a, b):
    answer = a+b
    return answer

def subract(a,b):
    answer = a-b
    return answer

def square_root(c):
    answer = math.sqrt(c)
    print(answer)

a = 15
b =3
sum = add(a,b)
diff = subract(a,b)
print("The sum of {} and {} is {}".format(a,b,sum))
print("The difference of {} and {} is {}".format(a,b,diff))
square_root(25)
