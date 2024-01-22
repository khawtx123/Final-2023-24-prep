from functools import reduce
def sum_of_squares_iteration(n):
    result = 1
    for i in range(1,n+1): result *= i*i
    return result
def sum_of_squares_recursive(n):
    if n ==1:return n
    else:
        return (n*n)*sum_of_squares_recursive(n-1)
def sum_of_squares_reduction(n):
    terms = []
    for i in range(1,n+1):terms.append(i*i)
    result = reduce(lambda x,y: x*y, terms)
    return result

result = sum_of_squares_reduction(3)

#Using dict
A = "8643"
encoding_scheme = {0:1, 1:5, 2:7, 3:0, 4:3, 5:9,
                   6:2, 7:6, 8:4, 9:8}

for i in range(len(A)):
    word = encoding_scheme[int(A[i])]
    print(word, end = '')

