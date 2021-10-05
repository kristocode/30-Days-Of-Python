### Exercises: Level 1

#1. Inside 30DaysOfPython create a folder called day_2. Inside this folder create a file named variables.py
#2. Write a python comment saying 'Day 2: 30 Days of python programming'
# 'Day 2: 30 Days of python programming'
#3. Declare a first name variable and assign a value to it
first_name = 'Elon'
#4. Declare a last name variable and assign a value to it
last_name = 'Musk'
#5. Declare a full name variable and assign a value to it
full_name  = {'f_name' : first_name,
              'l_name' : last_name }
#6. Declare a country variable and assign a value to it
country = 'South Africa'
#7. Declare a city variable and assign a value to it
city = 'Pretoria'
#8. Declare an age variable and assign a value to it
age = 50
#9. Declare a year variable and assign a value to it
year = 2021
#10. Declare a variable is_married and assign a value to it
is_married = False
#11. Declare a variable is_true and assign a value to it
is_true = True
#12. Declare a variable is_light_on and assign a value to it
is_light_on = False
#13. Declare multiple variable on one line
fruit, color, count, _set, calc = 'orange', 'blue', 12, {1, 3, 5}, 543.89

print('First Name: ', first_name)
print('Last Name: ', last_name)
print('Full Name: ', full_name)
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Year:', year)
print('Is married:', is_married)
print('Is True:', is_true)
print('Is Light On:', is_light_on, '\n')
### Exercises: Level 2

#1. Check the data type of all your variables using type() built-in function
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_light_on))
print(type(fruit))
print(type(color))
print(type(count))
print(type(color))


#1. Using the _len()_ built-in function, find the length of your first name
print('len ', len(first_name))
#1. Compare the length of your first name and your last name
print('which is the longest of the two?', len(first_name) == len(last_name))
#1. Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4
    # 1. Add num_one and num_two and assign the value to a variable total
total = num_one + num_two
print('total(num_one + num_two) : ', total)
    # 2. Subtract num_two from num_one and assign the value to a variable diff
diff = num_one - num_two    
print('diff(num_one - num_two) : ', diff)
    # 3. Multiply num_two and num_one and assign the value to a variable product
product =  num_two * num_one    
print('product(num_two * num_one) : ', product)
    # 4. Divide num_one by num_two and assign the value to a variable division
division = num_one / num_two   
print('division(num_one / num_two) : ', division) 
    # 5. Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder =  num_two % num_one   
print('remainder(num_two % num_one) : ', remainder) 
    # 6. Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one ** num_two 
print('exp(num_one ** num_two) : ', exp)   
    # 7. Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two    
print('floor_division(num_one // num_two) : ', floor_division)
# 1. The radius of a circle is 30 meters.
radius = 30
print('radius : ', radius)
    # 1. Calculate the area of a circle and assign the value to a variable name of _area_of_circle_
pi = 3.141592653589793  
_area_of_circle_ =  pi * (radius**2)  
print('Area of circle (pi*radius**2) : ', _area_of_circle_) 
    # 2. Calculate the circumference of a circle and assign the value to a variable name of _circum_of_circle_
diameter = radius*2    
_circum_of_circle_ =  pi * diameter
print('Circum of circle (pi*2*radius) : ',_circum_of_circle_)
    # 3. Take radius as user input and calculate the area.
i_radius = float(input('Enter radius of the circle: '))
area = pi * (i_radius**2) 
print('Area of circle : ', area)
# 1. Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
i_first_name = input('Enter first name : ')
i_last_name = input('Enter last name : ')
i_country = input('Enter country : ')
i_age = input('Enter age : ')

print('First Name Entry : ', i_first_name)
print('Last Name Entry : ', i_last_name)
print('Country Entry : ', i_country)
print('Age Entry : ', i_age)

# 1. Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
print(help('keywords'))