
a = "the sky is blue"
print(a)

#for letter in a:
#    print(letter)


def function_name():
    try:
        from my_calculator import sqrt
    except ModuleNotFoundError:
        from math import sqrt
    x = sqrt(4)
    print(x)

    dic = {"hello": 1,
           "goodbye": 2}
    
    try:
        print(dic["hi"])
    except KeyError:
        print(dic["hello"])

def main():
    function_name()

def add_positive_integers(a, b):
    if a < 0 or b<0:
        raise ValueError("Cannot add negative numbers")
    if type(a) is not int or type(b) is not int:
        raise TypeError("Cannot add non-integers")
    return a+b


if __name__ == "__main__":
    main()
    y = add_positive_integers(-2,4)


