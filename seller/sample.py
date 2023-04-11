def divide_decorator(func):
    def wrapper(n1,n2):
        if n2>n1:
            n1,n2 = n2,n1
        return func(n1,n2)
    return wrapper

@divide_decorator
def divide(m1, m2):
    result = m1/m2
    return result

a = divide (50,500)
print (a)
