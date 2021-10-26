## 💻 Exercises: Day 11

### Exercises: Level 1

# 1. Declare a function _add_two_numbers_. It takes two parameters and it returns a sum.
print('#1')
def add_two_numbers(a, b):
    return a+b
print('Sum two numbers : ', add_two_numbers(4, 5), '\n')

# 2. Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates _area_of_circle_.
print('#2')
import math 
def area_of_circle(radio):
    return math.pi * 2 * radio
print('Area of a circle : ', area_of_circle(5), '\n')

# 3. Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. 
# Check if all the list items are number types. If not do give a reasonable feedback.
print('#3')
#print(type(0) == number)
def add_all_nums(*params):
    sum = 0
    for param in params:
        if not isinstance(param, (int, float, complex) ):
            #raise(TypeError, 'param, is not numeric')
            print(f'{param} is not numeric')
        else:
            sum += param
    return sum
print('Sum of all summable arguments : ', add_all_nums(7,'8',9), '\n')

# 4. Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. 
# Write a function which converts °C to °F, _convert_celsius_to-fahrenheit_.
print('#4')
def convert_celsius_to_fahrenheit(celsius):
    return (float(celsius) * (9/5)) + 32

print('Convert celsius to fahrenheit : ', convert_celsius_to_fahrenheit(5), '\n')
# 5. Write a function called check-season, it takes a month parameter and returns the season: 
# Autumn, Winter, Spring or Summer.
print('#5')

def check_season(month):
    month = month.lower()
    if month in ['september','october','november']:
        return 'Spring'
    elif month in ['december','january','february']:
        return 'Summer'
    elif month in ['march','april','may']:
        return 'Autumn'
    elif month in ['june','july','august']:
        return 'Winter'
    else:
        return None

print(check_season('APRIL'))
print(check_season('JuLy'))
print(check_season('this isn\'t a month'), '\n')
# 6. Write a function called calculate_slope which return the slope of a linear equation
print('#6')
def calculate_slope(a, b):
    # y = mx + b 
    # m : slope => m = (y2-y1)/(x2-x1)
    slope = (p2[1] - p1[1]) / (p2[0] - p1[0])
    return slope

p1 = (2, 2)
p2 = (6, 10)
print(f'the slope between {p1} and {p2} is : ',calculate_slope(p1, p2), '\n')
# 7. Quadratic equation is calculated as follows: ax² + bx + c = 0. 
# Write a function which calculates solution set of a quadratic equation, _solve_quadratic_eqn_.
print('#7')
def solve_quadratic_eqn(a, b, c):
    r1 = (-b + ((b**2) - 4 * a * c))/ 2 * a
    r2 = (-b - ((b**2) - 4 * a * c))/ 2 * a
    return (r1, r2)

a = 1
b = 6
c = 9
print(f'Solution set of a quadratic equation for a={a}, b={b} and c={c} => {solve_quadratic_eqn(a, b, c)}')
a = 2
b = 5
c = 4
print(f'Solution set of a quadratic equation for a={a}, b={b} and c={c} => {solve_quadratic_eqn(a, b, c)} \n')

# 8. Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
print('#8')
def print_list(list):
    for l in range(len(list)):
        print(list[l], end=" - ") if(l<len(list)-1) else print(list[l], end="\n\n")

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]        
print('Elements of the list : ', end="")  
print_list(ages)      
# 9. Declare a function named reverse_list. 
# It takes an array as a parameter and it returns the reverse of the array (use loops).
print('#9')
""" py
print(reverse_list([1, 2, 3, 4, 5]))
# [5, 4, 3, 2, 1]
print(reverse_list1(["A", "B", "C"]))
# ["C", "B", "A"]
 """
def reverse_list(array):
    aux = []
    for a in array:
        aux.insert(0, a)
    return aux

print(reverse_list([1, 2, 3, 4, 5]))
print(reverse_list(["A", "B", "C"]),'\n')
# 10. Declare a function named capitalize_list_items. 
# It takes a list as a parameter and it returns a capitalized list of items
print('#10')
def capitalize_list_items(array): 
    aux = []   
    for a in array:
        if type(a) == str: 
            aux.append(a.capitalize())
    return aux
fruits = ['banana', 45.0, 'orange', 'mango', 9, 'lemon']
print(capitalize_list_items(fruits),'\n')

# 11. Declare a function named add_item. 
# It takes a list and an item parameters. It returns a list with the item added at the end.
print('#11')
'''py
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
numbers = [2, 3, 7, 9];
print(add_item(numbers, 5))      [2, 3, 7, 9, 5]
'''
def add_item(array, item):
    array.append(item)
    return array

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(add_item(food_staff, 'Meat')) 
numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))

# 12. Declare a function named remove_item. It takes a list and an item parameters. 
# It returns a list with the item removed from it.
print('#12')
'''py
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9];
print(remove_item(numbers, 3))  # [2, 7, 9]
'''
def remove_item(array, item):
    aux = []
    for i in array:
        if i != item:
            aux.append(i)
    return aux
            
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_staff, 'Mango'))
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3),'\n')  # [2, 7, 9]

#13. Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
print('#13')
'''py
print(sum_of_numbers(5))  # 15
print(sum_all_numbers(10)) # 55
print(sum_all_numbers(100)) # 5050
'''
def sum_of_numbers(nro):
    sum = 0
    for i in range(1,nro+1):        
        sum += i
    return sum

print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100),'\n') # 5050

# 14. Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
print('#14')
def sum_of_odds(nro):
    sum = 0
    for i in range(1,nro+1):        
        if(i % 2 != 0): # if is odd
            #print(i)
            sum += i
    return sum
print(sum_of_odds(5)) 
print(sum_of_odds(10)) # 
print(sum_of_odds(100),'\n')

# 15. Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
print('#15')

def sum_of_even(nro):
    sum = 0
    for i in range(1,nro+1):        
        if(i % 2 == 0): # if is even
            #print(i)
            sum += i
    return sum
print(sum_of_even(5)) 
print(sum_of_even(10)) # 
print(sum_of_even(100),'\n')
