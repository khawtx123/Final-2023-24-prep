#Ques 1
# HashMap - using a similar concept with dictionaries in python
#     {'BN' : [0,0,0,0,1,0,0,0,0,1],
#      'PN': [0, 1, 0, 0, 0, 1, 0, 1, 0, 1],
#      'PH': [1, 0, 1, 0, 0, 0, 1, 0, 1, 1],
#      }
# Easier to access compared to other data structures
# no point in using FIFO or LIFO data structures in determining number of votes per party
# HashMap can be encrypted to ensure data privacy
from functools import reduce

result =  {'BN' : [0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
     'PN': [0, 1, 0, 0, 0, 1, 0, 1, 0, 0],
     'PH': [1, 0, 1, 0, 0, 0, 1, 0, 1, 1],
     }

Vote = "Vote"
Count = "Count"
Percentage = "Percentage"
BN = "BN"
PH = "PH"
PN = "PN"
spoilt = "spoilt"
def processResult(result):
    sum_of_counts = 0
    spoilt_index = []
    skip = False
    for i in range(len(result['BN'])):
        sum_of_counts += result['PN'][i] + result['PH'][i] + result['BN'][i]
        if sum_of_counts > 1 or sum_of_counts == 0:
            spoilt_index.append(i)
        sum_of_counts = 0

    for spoil in spoilt_index:
        if not skip:
            del result['BN'][spoil]
            del result['PN'][spoil]
            del result['PH'][spoil]
            skip = True
        else:
            del result['BN'][spoil-1]
            del result['PN'][spoil-1]
            del result['PH'][spoil-1]

    print(f"{Vote:<10}  {Count:<10}  {Percentage:<10}")
    BN_result = reduce(lambda x,y: x+y, result['BN'])
    print(f"{BN:<11} 0{BN_result:<11}  {((BN_result/len(result['BN']))*100):<10.2f}")
    PN_result = reduce(lambda x, y: x + y, result['PN'])
    print(f"{PN:<11} 0{PN_result:<11}  {((PN_result / len(result['PN'])) * 100):<10.2f}")
    PH_result = reduce(lambda x, y: x + y, result['PH'])
    print(f"{PH:<11} 0{PH_result:<11}  {((PH_result / len(result['PH'])) * 100):<10.2f}")
    print(f"{spoilt:<11} 0{len(spoilt_index)}")

processResult(result)

#COrrected code

def m(x):
    return x

def f(x):
    return type(x) == complex

def r(x,y):
    if abs(x)>abs(y):
        return x
    else:
        return y

I = [3+4j, 'hello', -1j, 'world']
result = reduce(r,map(m, filter(f, I)))

print(result)