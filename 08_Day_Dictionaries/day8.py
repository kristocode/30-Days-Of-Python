## 💻 Exercises: Day 8
print(f'A dictionary is a collection of unordered, modifiable(mutable) paired (key: value) data type.\n')

# 1. Create  an empty dictionary called dog
dog = {}
print(f'Empty dictionary called dog : {dog}\n')

# 2. Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'Beto'
dog['color'] = 'Brown'
dog['breed'] = 'German Sheepdog'
dog['legs'] = 4
dog['age'] = 12
print(f'Dictionary called dog : {dog}\n')

# 3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, 
# country, city and address as keys for the dictionary
student = {
    'first_name' : 'Elon',
    'last_name'  : 'Musk', 
    'gender'     : 'Male',
    'age'        : 50,
    'marital satus' : 'Married',
    'skills'     : ['Engineer', 'Physicist'],
    'country'    : 'South Africa',
    'city'       : 'Pretoria',
    'address'    : 'Tesla 123'
}
# 4. Get the length of the student dictionary
print(f'student : {student}')
print(f'Length of the student dictionary : {len(student)}\n')

# 5. Get the value of skills and check the data type, it should be a list
print('student[skills] = ', student['skills'],' => type(student[skills] = ', type(student['skills']),'\n')

# 6. Modify the skills values by adding one or two skills
student['skills'].append('SEO')
student['skills'].append('Inventor')
print(f"Modify skills : {student['skills']} \n")

# 7. Get the dictionary keys as a list
keys = student.keys()
print(f'Keys as a list : {keys}\n')

# 8. Get the dictionary values as a list
values = student.values()
print(f'Values as a list : {values}\n')

# 9. Change the dictionary to a list of tuples using _items()_ method
print(f'Change the dictionary to a list of tuples using _items()_ method \n {student.items()} \n')

# 10. Delete one of the items in the dictionary
print(f'Delete last items in the dictionary : {student.popitem()}')

# 11. Delete one of the dictionaries
del dog
print(f'Delete dictionary called dog: {dog}')