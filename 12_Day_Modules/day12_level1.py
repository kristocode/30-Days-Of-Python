## 💻 Exercises: Day 12

### Exercises: Level 1

# 1. Write a function which generates a six digit/character random_user_id.
'''py
    print(random_user_id());
    '1ee33d'
'''
import string
import random 
def random_user_id(car=6):
    digits_letters = string.digits + string.ascii_letters
    return ''.join(random.choices(digits_letters,k=car))
        
print(random_user_id())
print(random_user_id(6), '\n')

# 2. Modify the previous task. Declare a function named user_id_gen_by_user. 
# It doesn’t take any parameters but it takes two inputs using input(). 
# One of the inputs is the number of characters and 
# the second input is the number of IDs which are supposed to be generated.
   
#py
#print(user_id_gen_by_user()) # user input: 5 5
#output:
#kcsy2
#SMFYb
#bWmeq
#ZXOYh
#2Rgxf
   
def user_id_gen_by_user():
    chars = int(input('Enter the number of characters : '))
    ids = int(input('Enter the number of IDs : '))
    output = ''
    for id in range(ids):
        output += random_user_id(chars) + '\n'
    return output

print(user_id_gen_by_user())    
#print(user_id_gen_by_user()) # 16 5
#1GCSgPLMaBAVQZ26
#YD7eFwNQKNs7qXaT
#ycArC5yrRupyG00S
#UbGxOFI7UXSWAyKN
#dIV0SSUTgAdKwStr


# 3. Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
   
'''py
print(rgb_color_gen())
# rgb(125,244,255) - the output should be in this form
'''
def rgb_color_gen():
    return tuple([random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)])

print(rgb_color_gen())