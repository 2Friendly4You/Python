#function for calculating factorial from a number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# calculate the factorial of number 1
print(factorial(1))