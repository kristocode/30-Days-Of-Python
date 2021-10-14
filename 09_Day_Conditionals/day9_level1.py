## 💻 Exercises: Day 9

### Exercises: Level 1

# 1.  Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: 
# You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
'''sh
Enter your age: 30
You are old enough to learn to drive.
Output:
Enter your age: 15
You need 3 more years to learn to drive.
'''
age = int(input('Enter your age: '))
if(age >= 18):
    print('You are old enough to learn to drive.\n')
else:
    print(f'You need {18-age} more years to learn to drive.\n')

# 2.  Compare the values of my_age and your_age using if … else. 
# Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. 
# You can use a nested condition to print 'year' for 1 year difference in age, 
# 'years' for bigger differences, and a custom text if my_age = your_age. Output:
'''sh
Enter your age: 30
You are 5 years older than me.
'''
age = int(input('Enter your age: '))
me = 25
if(age > me):
    rest =  age-me
    print("You are",rest,"year"+("s" if(rest>1) else ""),"older than me.\n")
elif (age == me):
    print("You are the same age as me\n")
else:
    rest =  me-age
    print("I am",rest,"year"+("s" if(rest>1) else ""),"older than you.\n")

# 3.  Get two numbers from the user using input prompt. 
# If a is greater than b return a is greater than b, 
# if a is less b return a is smaller than b, else a is equal to b. Output:

'''sh
Enter number one: 4
Enter number two: 3
4 is greater than 3
'''
one = int(input('Enter number one: '))
two = int(input('Enter number two: '))
if(one>two):
    print(f"{one} is greater than {two}")
elif (one<two):
    print(f"{one} is smaller than {two}")
else:
    print(f'{one} is equal to {two}')