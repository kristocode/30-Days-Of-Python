## 💻 Exercises: Day 10

### Exercises: Level 3

# 1. Go to the data folder and use the [countries.py]
# (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries.py) file. 
# Loop through the countries and extract all the countries containing the word _land_.

from countries import countries 
print('#1')
st_countries = set(countries) # Remove duplicate
lt_countries = list(st_countries)
lt_countries.sort()
#print(lt_countries,'\n')
for country in lt_countries:
    if('land' in country) :       
        print(country) 
print('\n')    

# 1. This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
print('#1')
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_reverse = []
for index in range(len(fruits)-1,-1,-1):
    fruits_reverse.append(fruits[index])    
print(fruits_reverse,'\n')

fruits_reverse.clear()
print(fruits_reverse,'\n')

for fruit in fruits:    
    fruits_reverse.insert(0, fruit)
print(fruits_reverse,'\n')

# 2. Go to the data folder and use the [countries_data.py]
# (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) file. 
print('#2')
from countries_data import countries_data
#    1. What are the total number of languages in the data
#print(countries_data)
print('#2.1')
unique = set()
for country in countries_data:    
    unique.update(country['languages'])
#print(f'Uniques languages : \n{unique}\n\n')
lst_unique = list(unique)
lst_unique.sort()
""" print(f'List Uniques languages : \n{lst_unique}\n')
for id in range(len(lst_unique)):
    print(id,' : ', lst_unique[id]) """
print(f'The total number of languages in the data is : {len(unique)}\n')

#    2. Find the ten most spoken languages from the data
print('#2.2')
all = []
for country in countries_data:    
    all += country['languages']
most_spoken = {}
for one in all:
    most_spoken[all.count(one)] = one
#print('most_spoken : ',most_spoken)
keys = list(most_spoken.keys())
keys.sort(reverse=True)
keys = keys[0:10]
#print(keys)
#print(most_spoken)
for key in keys:
    print(key,'\t',most_spoken[key] )
print('\n')    
#    3. Find the 10 most populated countries in the world
print('#2.3')
dct = {}
for country in countries_data:    
    dct[country['population']] = country['capital']
#print('dct : ',dct)    
keys = list(dct.keys())
keys.sort(reverse=True)
keys = keys[0:10]
#print(keys)
for key in keys:
    print(key,'\t',dct[key] )
print('\n')   