'''Exercise - Level 2 
Check the python version you are using'''
import os
print('Version python : ', os.system('python3 --version'))
import sys
print('Version python : ', sys.version)

'''Open the python interactive shell and do the following operations. The operands are 3 and 4.
addition(+)
subtraction(-)
multiplication(*)
modulus(%)
division(/)
exponential(**)
floor division operator(//) '''

x = 3
y = 4
print('addition(+): ', 3 + 4)
print('subtraction(-): ', 3 - 4)
print('multiplication(*): ', 3 * 4)
print('modulus(%): ', 3 % 4)
print('division(/): ', 3 / 4)
print('exponential(**): ', 3 ** 4)
print('floor division operator(//): ', 3 // 4)


'''Write strings on the python interactive shell. The strings are the following:
Your name
Your family name
Your country
I am enjoying 30 days of python'''

print('My name is ')
print('My family name is ')
print('My country is ')
print('My name is ')
print('I am enjoying 30 days of python')

'''Check the data types of the following data:
10
9.8
3.14
4 - 4j
['Asabeneh', 'Python', 'Finland']
Your name
Your family name
Your country'''

print(type(10))
print(type(9.8))
print(type(4 - 4j))
print(type(['Asabeneh', 'Python', 'Finland']))
print(type(''))
print(type(''))
print(type('Argentina'))