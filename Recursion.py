# def fact(x):
#     if x==1: return 1
#     else:
#         y = x*fact(x-1)
#         print(y)
#         return x*fact(x-1)
#
# fact(5)


# Recursion Dict
def factorial(n): # Calculate & return n!=n*(n-1)*..*1
    factorial_values_dict = {} # The cache
    # Get the value in cache, if it's already there
    if n in factorial_values_dict:
        f = factorial_values_dict[n]
        return f
    # If not, calculate & save in the cache
    else:
        if n ==1 :
            return 1
        else:
            f = n * factorial(n-1)
            factorial_values_dict[n] = f
            return f

print(factorial(3))