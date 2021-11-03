## 💻 Exercises: Day 12

### Exercises: Level 3
import random 
import string
#1. Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
def shuffle_list(lst):
    return random.sample(lst, k=len(lst))  # unique items
    #return random.choices(lst, k=len(lst)) # repeated items

original = [2, 3, 4, 6, 7]
print('original : ',original, ' - random : ',shuffle_list(original))
original = [2, '33', 4, 6, 7, 'blue', 12.3]
print('original : ',original, ' - random : ',shuffle_list(original), '\n')


#2. Write a function which returns an array of seven random numbers in a range of 0-9. 
# All the numbers must be unique.
def seven_unique_random_number():
    return random.sample(range(10), 7)

print(seven_unique_random_number()) 
print(seven_unique_random_number())  
print(seven_unique_random_number()) 
print(seven_unique_random_number())  
