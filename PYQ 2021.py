import random
from functools import reduce

def sos_iter(n):
    total = 1
    for i in range(1, n+1):
        total *= i*i
    return total

def sos_recursive(n):
    if n == 1:
        return 1
    else:
        return n*n*sos_recursive(n-1)

def sos_reduction(n):
    nums = []
    for i in range(1,n+1):
        nums.append(i*i)
    output = reduce(lambda x,y : x*y, nums)
    return output

print(sos_iter(3))
print(sos_recursive(3))
print(sos_reduction(3))

class Dice:
    instances = 0
    def __init__(self, min , max):
        Dice.instances += 1
        self.min = min
        self.max = max
        self.nums = []
        self.roll_counter = 0

    @staticmethod
    def displayCount():
        print(Dice.instances)

    def roll(self):
        i = random.randint(self.min, self.max)
        self.nums.append(i)
        self.roll_counter += 1
        return i

    def reset(self):
        self.roll_counter = 0
        self.nums = []

    def __str__(self):
        output = f"Dice's min value is {self.min}, Max is {self.max}. Dice has been rolled {self.roll_counter}, Sequence : {self.nums}"
        return output

    def getCurrentNumber(self):
        return self.nums[-1]

    def __mul__(self, other):
        total = 0
        for i in range(other):
            total += self.roll()
        return total

    def __add__(self, other):
        i1 = self.roll()
        i2 = other.roll()
        return i1+i2

d1 = Dice(1,6)
d2 = Dice(1,12)
Dice.displayCount()
print(d1)
d1.roll()
print(d1.getCurrentNumber())
print(d1)
d1.reset()
print(d1)
s = d1 * 2
print (s)
print(d1)
s = d1 + d2
print (s)
print (d1)
print (d2)