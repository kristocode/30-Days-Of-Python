## 💻 Exercises: Day 11

### Exercises: Level 3

# 1. Write a function called is_prime, which checks if a number is prime.
# A prime number is a number greater than 1 with only two factors – themselves and 1.
# A prime number cannot be divided by any other numbers without leaving a remainder.
def is_prime(number):    
    if number > 1:
        for i in range(2,number): # it does not include 1 or the same number.               
            if number%i == 0:
                return False   
        return True     
    else :
        return False
    

print('2 is prime :',is_prime(2))
print('5 is prime :',is_prime(5))
print('8 is prime :',is_prime(8))
print('19 is prime :',is_prime(19))
print('163 is prime :',is_prime(163))
print('181 is prime :',is_prime(181))
print('721 is prime :',is_prime(721), '\n')

# 2. Write a functions which checks if all items are unique in the list.
def unique(lst):
    for i in lst:
        if lst.count(i) > 1:
            return False
    return True
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
fruits = ['banana', 'orange', 'mango', 'lemon']
print('unique()' , unique(ages))
print('unique()' , unique(fruits), '\n')

# 3. Write a function which checks if all the items of the list are of the same data type.
def same_data_type(lst):
    if len(lst)>0 :
        tp = type(lst[0])
        #print('type(lst[0]) : ', tp)
        for i in range(1,len(lst)):            
            if tp != type(lst[i]):
                return False
        return True

several = [34, 'String', True, ]
print('same_data_type(ages)' , same_data_type(ages))
print('same_data_type(several)' , same_data_type(several))
print('same_data_type(fruits)' , same_data_type(fruits), '\n')  
        
# 4. Write a function which check if provided variable is a valid python variable
""" Python Variable Name Rules

A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (firstname, Firstname, FirstName and FIRSTNAME) are different variables) 
"""
def check_var(var):
    return var.isidentifier()

def check_variable(var):
    
    
    if(var[0].isalpha() or var[0] == '_' or not var[0].isdecimal()):
        for i in range(1, len(var)):
            print(var[i], end='')
            if not var[i].isalpha() and not var[i] == '_' and not var[i].isdecimal():
                return False
        return True
    return False

print('Let us se valid variable names:')
print('\nfirst_name is a variable : ', check_variable('firstname'))
print('\n_if is a variable : ', check_variable('_if'))
print('\ncurrent_year_2021 is a variable : ', check_variable('current_year_2021'))
print('\nyear_2021 is a variable : ', check_variable('year_2021'))
print('\nnum2 is a variable : ', check_variable('num2'), '\n')
print('\nInvalid variables names:')
print('\nfirst-name is a variable : ', check_variable('first-name'))
print('\nfirst@name is a variable : ', check_variable('first@name'))
print('\nfirst$name is a variable : ', check_variable('first$name'))
print('\nnum-1 is a variable : ', check_variable('num-1'))
print('\n1num is a variable : ', check_variable('1num'), '\n')

""" print('first-name is a variable : ', check_var('first-name'))
print('first@name is a variable : ', check_var('first@name'))
print('first$name is a variable : ', check_var('first$name'))
print('num-1 is a variable : ', check_var('num-1'))
print('1num is a variable : ', check_var('1num'))
 """

# 5. Go to the data folder and access the countries-data.py file.

# - Create a function called the most_spoken_languages in the world. 
# It should return 10 or 20 most spoken languages in the world in descending order
from data.Countries_data import Countries_data as c_d
print(c_d.cntrs_data)
""" def most_spoken_languages():
    all = []
    for country in c_d:    
        all += country['languages']
    most_spoken = {}
    for one in all:
        most_spoken[all.count(one)] = one
    #print('most_spoken : ',most_spoken)
    keys = list(most_spoken.keys())
    keys.sort(reverse=True)
    keys = keys[0:10]
    #print(keys)
    #print(most_spoken)
    for key in keys:
        print(key,'\t',most_spoken[key] )
    print('\n')  

print(most_spoken_languages())   """
#- Create a function called the most_populated_countries. 
# It should return 10 or 20 most populated countries in descending order.
""" def most_populated_countries():
    dct = {}
    for country in c_d:    
        dct[country['population']] = country['capital']
    #print('dct : ',dct)    
    keys = list(dct.keys())
    keys.sort(reverse=True)
    keys = keys[0:10]
    #print(keys)
    for key in keys:
        print(key,'\t',dct[key] )
    print('\n')    """