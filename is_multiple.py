#ask the user to enter a number that represents integer n
#ask the user to enter a number that represents integer m
#create a function with m, n, and i as parameters
#if n is a multiple of m return True
#False if otherwise

n = int(input("Enter a number that represents n: "))
m = int(input("Enter a number that represents m: "))
def is_multiple(m,n):
    if n % m == 0:
        return True
    else:
        return False
print(is_multiple(m,n))