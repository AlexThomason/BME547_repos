# returns.py
# Author Alex Thomason

def add1(a,b):
    c = a+b
    if c<0:
        return "This answer is negative"
    return c


answer = add1(3,-5)
print(answer)


def add2(a,b):
    c = a+b
    d = a-b
    return c,d


answer = add2(3,-5)
print(answer[0])
print(answer[1])

added, subtracted = add2(3,-5)
print(added)
print(subtracted)
