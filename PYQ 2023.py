from functools import reduce
from random import random

def multiply(x,y):
    return x*y

def squares(num):
    return num**2

def odd_num(num):
    return num%2 == 0

def mySort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def f(x):
    for i in range(x):
        print('A', end = '')

print("Generator Expression")
it = (f(i) for i in range(3))
for i in it:
    print('B', end= '')

print("List Comprehension")
It = [f(i) for i in range(3)]
for i in It:
    print('B', end= '')
print('')


def genRandomIntSeq(m):
    s = set()
    while True :
        i = int(random()*m)+1
        if i not in s:
            s.add(i)
            yield i
        if len(s) == m:
            break

print('Random Int Seq = [', end = '')
for j in genRandomIntSeq(5):
    print(j, end='')
print(']')

def getTopStudent(marks):
    highest_mark = 0
    winner = ''
    winner_lst = []
    for pairs in marks:
        if pairs[1] > highest_mark:
            winner =  pairs[0]
            highest_mark = pairs[1]
    winner_lst.append(winner)
    winner_lst.append(highest_mark)
    print(winner_lst)

def getTopStudentReduction(marks):
    marks_lst = []
    name_lst = []
    index_winner = 0
    for pairs in marks:
        name_lst.append(pairs[0])
        marks_lst.append(pairs[1])
    highest_mark = reduce(max , marks_lst)
    for i in range(len(marks_lst)):
        if highest_mark == marks_lst[i]:
            index_winner = i
            break
    winner = name_lst[index_winner]

    winner_lst = [winner, highest_mark]
    print(winner_lst)

marks = [['alice' , 95], ['bob', 100], ['candice' , 70]]

getTopStudent(marks)
getTopStudentReduction(marks)
print('RandomIntSeq = [', end = '')
for j in genRandomIntSeq(5):
    print(j, end='')
print(']')

it = (f(i) for i in range(3))

for i in it:
    print('B', end = '')

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

product = reduce(multiply, numbers)
product_lst = map(squares, numbers)
product_lst2 = filter(odd_num, numbers)

print(list(product_lst2))

# f(0) = None
# f(1) = A
# f(2) = AA
# Generator Expression : Memory is allocated on the fly
# List Comprehension : Memory allocated statically

class Wheel:
    def __init__(self, products):
        self.products = products
        self.products_order = []

    def display(self):
        for pair in self.products:
            print(f"{pair[0]}: {pair[1]}")

    def spin(self):
        product_quantities = 0
        for pair in self.products:
            product_quantities += pair[1]
        if product_quantities == 0:
            print("No more left")
        else:
            idx = int(random()*len(self.products))
            s = set()
            s.add(idx)
            if self.products[idx][1] == 0:
                idx = int(random() * len(self.products))
                while idx in s or self.products[idx][1] == 0:
                    idx = int(random() * len(self.products))

            print(f"Visitor wins product {self.products[idx][0]}")
            self.products_order.append(self.products[idx][0])
            self.products[idx][1] -= 1

    def trace(self):
        for product in self.products_order:
            print(product, end= '')
            if product == self.products_order[-1]:
                break
            print("->", end = '')

products = [["P1", 1], ["P2", 1], ["P3", 1]]
wheel = Wheel(products)
wheel.display()
wheel.spin()
wheel.spin()
wheel.spin()
wheel.spin()
wheel.spin()
wheel.trace()