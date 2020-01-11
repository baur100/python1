def is_prime(x):
    for i in range(2,x-1):
        if x%i==0:
            return False
    return True


def find_prime(x,y):
    for z in range(x,y):
        if is_prime(z):
            print(z)


find_prime(250,300)

