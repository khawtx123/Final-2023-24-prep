# python better than c++
#
# The comparison between Python and C++ depends on the context of use, the specific requirements of a project, and the goals of the programmer. Both Python and C++ are powerful programming languages, but they have different strengths and weaknesses. Here are some reasons why one might consider Python to be "better" than C++ in certain situations:
#
# 1. **Readability and Simplicity:**
#    - **Python:** Python is known for its clean and readable syntax. Its code is often more concise and easier to understand than equivalent C++ code. This can lead to faster development and easier maintenance.
#
#    - **C++:** C++ syntax can be more complex, and programs tend to be longer due to explicit type declarations and lower-level memory management.
#
# 2. **Ease of Learning:**
#    - **Python:** Python is considered more beginner-friendly. Its simple syntax and high-level abstractions make it easier for newcomers to grasp programming concepts.
#
#    - **C++:** C++ has a steeper learning curve, especially for beginners. It requires a solid understanding of low-level concepts like pointers, memory management, and explicit typing.
#
# 3. **Rapid Development:**
#    - **Python:** Python is often chosen for rapid development, prototyping, and scripting tasks. Its dynamic typing and high-level abstractions allow developers to write code quickly.
#
#    - **C++:** While C++ can be used for rapid development, its focus on low-level details and explicitness may slow down the development process compared to Python.
#
# 4. **Community and Libraries:**
#    - **Python:** Python has a large and active community. It offers a vast ecosystem of libraries and frameworks for various domains, including web development, data science, machine learning, and more.
#
#    - **C++:** C++ has a strong community, but it may not be as extensive as Python's for certain domains. However, C++ has a rich set of libraries, especially in areas like systems programming and game development.
#
# 5. **Portability:**
#    - **Python:** Python is often considered more portable as it is an interpreted language. Python programs can run on any platform with a Python interpreter.
#
#    - **C++:** C++ programs need to be compiled for a specific platform, and binary compatibility may be a concern when moving between different systems.
#
# 6. **Memory Management:**
#    - **Python:** Python has automatic memory management (garbage collection), simplifying memory-related issues for developers.
#
#    - **C++:** C++ allows manual memory management, which provides fine-grained control but can lead to memory-related bugs if not handled carefully.
#
# It's important to note that the choice between Python and C++ depends on the project requirements. While Python is often preferred for tasks like web development, data analysis, and scripting, C++ is commonly used for performance-critical applications, systems programming, game development, and situations where low-level control over hardware is essential. Each language has its strengths, and the best choice depends on the specific needs of the project.
from functools import reduce

import QtWidgets as QtWidgets


def cube(n):
    while True:
        yield n*n*n
        if n>0:
            n = n -1
        # the ques didnt add else: break, so the output is nothing
        else:
            break
total = 0
for i in cube(3):
    total = total + i
print(total)

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n*factorial(n-1)

def approx_e(n_terms):
    sum_terms = 0
    for term in range(n_terms+1):
        sum_terms += 1/factorial(term)
    print(sum_terms)
    return sum_terms

def approx_e_recursive(n_terms):
    if n_terms==0:
        return 1
    else: return  1/factorial(n_terms)+approx_e(n_terms-1)

def sumOfNumber(x,y):
    return x+y

def approx_e_reduction(n_terms):
    terms = []
    for i in range(n_terms):
        terms.append(1/factorial(i))
    return reduce(sumOfNumber, terms)

approx_e(8)
print(approx_e_recursive(8))
print(approx_e_reduction(8))

class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients
        self.reversed_coefficients = []
        self.power = []


    def __str__(self):
        output = ""
        first_term = False
        for i in range(len(self.coefficients)):
            x = -(i + 1) #-1, -2, -3
            power = x+len(self.coefficients)
            if not first_term:
                if power>1: output += f"{self.coefficients[x]}x^{power}"
                elif power==1: output += f"{self.coefficients[x]}x"
                else: output += f"{self.coefficients[x]}"
                first_term = True
            else:
                if self.coefficients[x] >0: output += "+"
                else: output += "-"
                if power>1: output += f"{self.coefficients[x]}x^{power}"
                elif power==1: output += f"{self.coefficients[x]}x"
                else: output += f"{self.coefficients[x]}"

            self.reversed_coefficients.append(coefficients[x])
            self.power.append(power)

        return output

    def eval(self, param):
        total = 0
        for i in range(len(self.power)):
            total += self.reversed_coefficients[i]*pow(param, self.power[i])
        print(total)
        return total

    def __mul__(self, other):
        new_coefficients = []
        for i in range(len(self.coefficients)):
            new_coefficients.append(self.coefficients[i]*other)
        p2 = Polynomial(new_coefficients)
        print(p2)
        return p2

    def __truediv__(self, other):
        new_coefficients = []
        for i in range(len(self.coefficients)):
            new_coefficients.append(self.coefficients[i]/other)
        p2 = Polynomial(new_coefficients)
        print(p2)
        return p2

    def __add__(self, other):
        new_coefficients = []
        i = 0
        for term in self.coefficients:
            new_coefficients.append(term+other.coefficients[i])
            i+=1
        p2 = Polynomial(new_coefficients)
        print(p2)
        return p2

    def __sub__(self, other):
        new_coefficients = []
        i = 0
        for term in self.coefficients:
            new_coefficients.append(term-other.coefficients[i])
            i+=1
        p2 = Polynomial(new_coefficients)
        print(p2)
        return p2
coefficients = [1, 2, 3, 4]
eqn = Polynomial(coefficients)
print(eqn)
eqn.eval(3)

eqn2 = eqn*2
eqn3 = eqn/2
eqn4 = eqn + eqn2
eqn4 -= eqn2

