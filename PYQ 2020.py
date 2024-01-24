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
    for i in range(1,2*(n)):
        if isOdd(i): lst.append(i)
    return reduce(lambda x,y: x*y, lst)

print(mul_of_odds_reduction(4))
print(mul_of_odss_recursive(4))


class Shapes:
    def __init__(self, b, h):
        self.b = b
        self.h = h
    def calcArea(self):
        return self.b * self.h

class Circle(Shapes):
    def __init__(self, b, h):
        Shapes.__init__(self, b, h)

    def calcArea(self):
        return (2*3.142*self.b)

class Sphere:
    def __init__(self, radius):
        self.radius = radius
        self.volume = self.calcVolume()

    def calcVolume(self):
        return ((4/3)*3.142*pow(self.radius, 3))

    def __eq__(self, other):
        return other.volume == self.volume

    def __str__(self):
        str = f"Radius is {self.radius}, Volume is {self.volume}"
        return str

    def __mul__(self, other):
        vol = self.volume*other
        radius = pow((3*vol)/(4*3.142), 1/3)
        return Sphere(radius)

    def __add__(self, other):
        vol = self.volume + other.volume
        radius = pow((3 * vol) / (4 * 3.142), 1 / 3)
        return Sphere(radius)


s1 = Sphere(2)
s2 = Sphere(2)
s3 = s1 +s2
s4 = s1*2
print(s3)
print(s4)