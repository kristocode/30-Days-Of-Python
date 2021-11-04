## 💻 Exercises: Day 13

# # 1. Filter only negative and zero in the list using list comprehension
'''py
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
'''
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative = [i for i in numbers if i <= 0]
print(negative,'\n')
# # 2. Flatten the following list of lists of lists to a one dimensional list :
'''py
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

output
[1, 2, 3, 4, 5, 6, 7, 8, 9]
'''
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flatten = [i for d1 in list_of_lists for d2 in d1 for i in d2]
print(flatten,'\n')
# # 3. Using list comprehension create the following list of tuples:
'''py
[(0, 1, 0, 0, 0, 0, 0),
(1, 1, 1, 1, 1, 1, 1),
(2, 1, 2, 4, 8, 16, 32),
(3, 1, 3, 9, 27, 81, 243),
(4, 1, 4, 16, 64, 256, 1024),
(5, 1, 5, 25, 125, 625, 3125),
(6, 1, 6, 36, 216, 1296, 7776),
(7, 1, 7, 49, 343, 2401, 16807),
(8, 1, 8, 64, 512, 4096, 32768),
(9, 1, 9, 81, 729, 6561, 59049),
(10, 1, 10, 100, 1000, 10000, 100000)]
'''

tpl = [ tuple( [i] + [i**j for j in range(6) ])for i in range(11) ]
print(tpl,'\n')

# 4. Flatten the following list to a new list:
'''py
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
output:
[['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
'''
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
new = [[lst[0][0].upper(),lst[0][0].upper()[0:3],lst[0][1].upper() ] for lst in countries ]
print(new, '\n')

# 5. Change the following list to a list of dictionaries:
'''py
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
output:
[{'country': 'FINLAND', 'city': 'HELSINKI'},
{'country': 'SWEDEN', 'city': 'STOCKHOLM'},
{'country': 'NORWAY', 'city': 'OSLO'}]
'''
output = [{'country': lst[0][0].upper(), 'city': lst[0][1].upper()} for lst in countries ]
print(output, '\n')

# 6. Change the following list of lists to a list of concatenated strings:
'''py
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
output
['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']
'''
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
first_last_name = [ ' '.join(lst[0])  for lst in names  ]
print(first_last_name, '\n')

# 7. Write a lambda function which can solve a slope or y-intercept of linear functions.
slope = lambda a, b: (b[1] - a[1]) / (b[0] - a[0])
    # y = mx + b 
    # m : slope => m = (y2-y1)/(x2-x1)
    # y-intercept => p(x, 0) => 0 = mx + b => x = -b/m

p1 = (2, 2)
p2 = (6, 10)
print(f'the slope between {p1} and {p2} is : ', slope(p1, p2), '\n')
