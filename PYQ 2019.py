# statement is complete line of code that performs an action.
# executed by compiler or interpreter
# statement include expression

# Expression is a piece of code that produces a value
# it consists of variables constants and operators and func calls
# func calls or arithmetic operations

def Func(x):
    total = 0
    for i in range(x):
        total += i*(i-1)
    return total

print(Func(5))

# Lazy do b(ii)

counter = 0

while counter <101:
    if counter % 2 == 0:
        counter += 1
    else:
        counter += 2

#Corrected Code
sentence, i = "that car was really fast", 1
while i > 0:
    for character in sentence:
        if character == "t":
            print("found !")
        else:
            print("maybe next")
    i = 0


L = [1, 2, 3, 4]
print(''.join([str(i) for i in L]))

#Corrected Code
lower = input("Enter lower range: ")
upper = input("Enter higher range: ")

lower = int(lower)
upper = int(upper)
print("Prime numbers are: ")

for num in range(lower, upper):
    prime = True
    if num>1:
        for i in range(2, num):
            if(num%i) == 0:
                prime = False
                break
        if prime: print(num)
    else: print(num)

def factorial(x):
    if x <= 1:
        return 1
    else:
        return x*factorial(x-1)

print(factorial(5))