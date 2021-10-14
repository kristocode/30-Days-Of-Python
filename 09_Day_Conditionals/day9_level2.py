## 💻 Exercises: Day 9

### Exercises: Level 2

#1. Write a code which gives grade to students according to theirs scores:
   
'''sh
80-100, A
70-89, B
60-69, C
50-59, D
0-49, F
'''
score = int(input('Enter your score: '))
if(80<=score<=100):
    print("A")
elif(70<=score<=79):
    print("B")
elif(60<=score<=69):
    print("C")
elif(50<=score<=59):
    print("D")
else:
    print("F")

# 1. Check if the season is Autumn, Winter, Spring or Summer. If the user input is:
""" September, October or November, the season is Autumn.
December, January or February, the season is Winter.
March, April or May, the season is Spring
June, July or August, the season is Summer """
Autumn = ['September','October','November']
Winter = ['December','January','February']
Spring = ['March','April','May']
Summer = ['June','July','August']
month = input('Enter month : ').capitalize()
if(month in Autumn):
    print('The season is Autumn')
elif(month in Winter):
    print('The season is Winter')
elif(month in Spring):
    print('The season is Spring')
elif(month in Summer):
    print('The season is Summer')
else:
    print("You entered the month wrong")

# 2.  The following list contains some fruits:
'''sh'''
fruits = ['banana', 'orange', 'mango', 'lemon']

# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. 
fruit =  input("Enter a fruit: ").lower()
if(fruit not in fruits):
    fruits.append(fruit)
    print(f"Add the fruit({fruit}) to the list :\n {fruits}")

# If the fruit exists print('That fruit already exist in the list') 
if(fruit in fruits):
    print(f'That fruit({fruit}) already exist in the list\n {fruits}')