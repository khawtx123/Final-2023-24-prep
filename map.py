k = map(int, [1.4, 5.6])

def even(n):
    n_new = n%2
    return n_new

evens = filter(even, range(1,11))
print(list(evens))
print(list(k))