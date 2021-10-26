#1. Declare your age as integer variable
age = 42
#2. Declare your height as a float variable
height = 1.79
#3. Declare a variable that store a complex number
complex = 2 + 5j
#4. Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).

'''py
    Enter base: 20
    Enter height: 10
    The area of the triangle is 100
'''
base = float(input('Enter base : '))
height = float(input('Enter height : '))
area = 0.5 * base * height
print('Area of triangle : ', area)

# 5. Write a script that prompts the user to enter side a, side b, and side c of the triangle. 
# Calculate the perimeter of the triangle (perimeter = a + b + c).

'''py
Enter side a: 5
Enter side b: 4
Enter side c: 3
The perimeter of the triangle is 12
'''
side_a = float(input('Enter side a : '))
side_b = float(input('Enter side b : '))
side_c = float(input('Enter side c : '))
perimeter = side_a + side_b + side_c
print('The perimeter of the triangle is : ', perimeter)

# 6. Get length and width of a rectangle using prompt. 
# Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length = float(input('Enter length of the rectangle : '))
width = float(input('Enter width of the rectangle : '))
area_r = length * width
perimeter_r = 2 * area_r 
print('The area of rectangle is : ', area_r)
print('The perimeter of rectangle is: ', perimeter_r)
# 7. Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and 
# circumference (c = 2 x pi x r) where pi = 3.14.
import math
radius_c = float(input('Enter radius of the circle : '))
area_c = 2 * radius_c * math.pi
print('The area of the circle is : ', area_c)
circumference = 2 * math.pi * radius_c
print('The circumference of the circle is : ', circumference) 
# 8. Calculate the slope, x-intercept and y-intercept of y = 2x -2
# x-intercept is when y = 0 then x = 2/2
x_intercept = 2/2
# y-intercept is when x = 0 then y = -2
y_intercept = -2
# slope = y-intercept/x-intercept
slope = y_intercept / x_intercept
print('x-intercept (0=2x-2) is ', x_intercept)
print('y-intercept (y=2(0)-2) is ', y_intercept)
print('Slope is ', slope) 
# 9. Slope is (m = y2-y1/x2-x1). Find the slope and [Euclidean distance]
# (https://en.wikipedia.org/wiki/Euclidean_distance#:~:text=In%20mathematics%2C%20the%20Euclidean%20distance,being%20called%20the%20Pythagorean%20distance.) 
# between point (2, 2) and point (6,10) 
p1 = (2, 2)
p2 = (6, 10)
import math
slope_ = (p2[1] - p1[1]) / (p2[0] - p1[0])
print('Slope is : ', slope_ )
base = (p2[0] - p1[0]) + (p2[1] - p1[1])
dE = math.pow( base, 0.5)
print(f'Euclidian distance between {p1} and {p2} is : ', dE) 
# 10. Compare the slopes in tasks 8 and 9.
print(f'Compare {slope} with {slope_} if equal : ', slope == slope_)
# 11. Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
x0 = 0
x1 = 1
x5 = 5
y0 = x0**2 + 6*x0 + 9
y1 = x1**2 + 6*x1 + 9
y5 = x5**2 + 6*x5 + 9
print(f'Value calculate for x0={x0} on function y = x^2 + 6x + 9 is y0= ',y0 )
print(f'Value calculate for x1={x1} on function y = x^2 + 6x + 9 is y2= ',y1 )
print(f'Value calculate for x5={x5} on function y = x^2 + 6x + 9 is y5= ',y5 )
a = 1
b = 6
c = 9
r1 = (-b + ((b**2) - 4 * a * c))/ 2 * a
r2 = (-b - ((b**2) - 4 * a * c))/ 2 * a
print('First root for function (y = x^2 + 6x + 9) is r1=', r1)
print('Second root for function (y = x^2 + 6x + 9) is r2=', r2)
# 12. Find the length of 'python' and 'dragon' and make a falsy comparison statement.
print("Is length('python') = length('dragon')? : ", len('python') == len('dragon'))
# 13. Use _and_ operator to check if 'on' is found in both 'python' and 'dragon'
result1 = 'on' in 'python'
print('result1 : ', result1)
result2 = 'on' in 'dragon'
print('result2 : ', result2)
print("Check if 'on' is found in both 'python' and 'dragon' : ", result1 & result2)
# 14. _I hope this course is not full of jargon_. Use _in_ operator to check if _jargon_ is in the sentence.
sentence = 'I hope this course is not full of jargon'
print('jargon is in the sentence? ', 'jargon' in sentence)
# 15. There is no 'on' in both dragon and python
result3 = 'on' not in 'python'
print('result1 : ', result3)
result4 = 'on' not in 'dragon'
print('result2 : ', result4)
print("There is no 'on' in both 'python' and 'dragon' : ", (result3 & result4))
# 16. Find the length of the text _python_ and convert the value to float and convert it to string
text_to_float = float(len('python'))
text_to_str = str(len('python'))
print("Convert length of the text 'python' to float : ", text_to_float ," of type ", type(text_to_float))
print(f"Convert length of the text 'python' to string : {text_to_str} of type {type(text_to_str)}")
# 17. Even numbers are divisible by 2 and the remainder is zero. 
# How do you check if a number is even or not using python?
num1 = int(input('Enter a number integer to know if it is even : '))
print(f'Is even number {num1} ? : ', (num1 % 2) == 0)
# 18. Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
print('Floor division (7 // 3) is : ', (7//3))
print('value 2.7 converted to the int : ', int(2.7))
print('Check if (7//3) = int(2.7) : ', (7//3) == int(2.7))
# 19. Check if type of '10' is equal to type of 10
print("Check if type of '10' is equal to type of 10 : ", type('10') == type(10))
# 20. Check if int('9.8') is equal to 10
#int_ = int('9.8') 
# ValueError: invalid literal for int() with base 10: '9.8'
#print('int_ : ', int_)
#print("Check if int('9.8') is equal to 10 : ", int_ == 10)
# 21. Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?

'''py
Enter hours: 40
Enter rate per hour: 28
Your weekly earning is 1120
'''
hours = int(input('Enter hours : '))
rate_per_hour = float(input('Enter rate per hour : '))
print('Your weekly earning is : ', hours * rate_per_hour)
# 22. Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years

'''py
Enter number of years you have lived: 100
You have lived for 3153600000 seconds.
'''
sec_min = 60 # seconds
sec_hour = 60 * sec_min # 3600 seconds in an hour
sec_day = 24 * sec_hour
sec_year = 365 * sec_day 
year_old = int(input('Enter number of years you have lived : '))
print(f'You have lived for {year_old * sec_year} seconds')

# 23. Write a Python script that displays the following table

'''py
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
'''

lista = [1, 2, 3, 4, 5]
for i in lista: 
    print(i , end=' ')       
    for j in range(4):
        print(i**j, end=' ' )
    print()