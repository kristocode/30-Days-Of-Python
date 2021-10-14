## 💻 Exercises: Day 9

### Exercises: Level 3

# 1. Here we have a person dictionary. Feel free to modify it!
   
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}


# * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
#print(type(person['skills']), '\n')

if('skills' in person and type(person['skills']) == list ):
    length = (len(person['skills'])-1)//2
    if(len(person['skills'])%2 != 0):
        print(f"Has skills key and the middle skill is : {person['skills'][length]}\n")
    else:
        print(f"Has skills key and the middle skills are : {person['skills'][length]}, {person['skills'][length+1]}\n")        
else:
    print(f"Hasn't skills key\n")

# * Check if the person dictionary has skills key, 
# if so check if the person has 'Python' skill and print out the result.
if('skills' in person and type(person['skills']) == list ): 
    print('Has skills key')   
    print("And has 'Python' skill\n" if('Python' in person['skills']) else "And hasn't 'Python' skill\n")
else:
    print('Hasn\'t skills key\n')

# * If a person skills has only JavaScript and React, print('He is a front end developer'), 
# if the person skills has Node, Python, MongoDB, print('He is a backend developer'), 
# if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), 
# else print('unknown title') - for more accurate results more conditions can be nested!
st0 = set(person['skills'])
st1 = {'JavaScript', 'React'}
st2 = {'Node', 'Python', 'MongoDB'}
st3 = {'React', 'Node', 'MongoDB'}
if(st1.issubset(st0)):
    print('He is a front end developer\n')
if(st2.issubset(st0)):
    print('He is a backend developer\n')
if(st3.issubset(st0)):
    print('He is a fullstack developer\n')
else:
    print('unknown title\n')

# * If the person is married and if he lives in Finland, print the information in the following format:
'''py
    Asabeneh Yetayeh lives in Finland. He is married.
'''

if(person['is_marred'] and person['country'] == 'Finland'):
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")
