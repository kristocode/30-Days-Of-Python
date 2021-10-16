## 💻 Exercises: Day 10

### Exercises: Level 2
    
# 1.  Use for loop to iterate from 0 to 100 and print the sum of all numbers.

'''sh
The sum of all numbers is 5050.
'''
sum = 0
for i in range(101):
    sum += i
print(f'sum = {sum}\n')

# 1. Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
sum_evens = 0
sum_odds = 0
for i in range(101):
    if(i%2 == 0):
        sum_evens += i  
    else: 
        sum_odds += i
print(f'sum_evens = {sum_evens}\n')
print(f'sum_odds = {sum_odds}\n')
'''sh
The sum of all evens is 2550. And the sum of all odds is 2500.
'''
