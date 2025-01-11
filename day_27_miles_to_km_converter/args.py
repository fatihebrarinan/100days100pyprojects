def add(*args):
    sum = 0
    for i in args:
        sum += i
    print(sum)
add(1,2,3,5,6,7,7,8,8)

# args are tuple

def calculate(n, **kwargs):
    # for (key,value) in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)

# kwargs are dictionaries
