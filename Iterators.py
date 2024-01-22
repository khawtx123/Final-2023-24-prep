def fruits(n):
    for x in n:
        yield '%s' % x

fruit = ['apple', 'orange', 'pear']
f = fruits(fruit)

for x in f:
    print(x)
