import random
from functools import reduce

for i in range(2,11):
    x = 1
    for j in range(2,i):
        n = i%j
        if n == 0:
            x = 0
            break
    if x ==1:
        print(i)

i = random.randint(1,10)
tries = 1
while tries <= 5:
    break
    user_input = int(input(f"The {tries}th try: "))
    if user_input == i:
        print(f"Correct! You got it in try {tries}")
    else:
        print("wrong")
        if user_input < i:
            print("its higher")
        else:
            print("its lower")
    tries += 1

print("suck my dick bitch")

def sumOfNumber(x,y):
    return x+y
A = [True, 1.0, 3, "Hi", 3+4j]
def isNumber(x):
    if type(x) == float: return 1
    elif type(x) == complex:return 1
    elif type(x) == int:return 1
    else:return 0
B = filter(isNumber, A)
result = reduce(sumOfNumber,map(lambda x: x,B))
print(result)


def isOdd(n):
    if n%2==1: return True
def mul_of_odss_recursive(n):
    if n <=1:return 1
    else: return (2*n-1)*mul_of_odss_recursive(n-1)
def mul_of_odds_reduction(n):
    lst = []
    for i in range(1,2*(n+1)-1):
        if isOdd(i): lst.append(i)
    return reduce(lambda x,y: x*y, lst)

print(mul_of_odds_reduction(3))
print(mul_of_odss_recursive(3))
