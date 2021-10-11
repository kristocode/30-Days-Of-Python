### Exercises: Level 3
age = [22, 19, 24, 25, 26, 24, 25, 24]
""" There are four collection data types in Python :

List: is a collection which is ordered and changeable(modifiable). Allows duplicate members.
Tuple: is a collection which is ordered and unchangeable or unmodifiable(immutable). Allows duplicate members.
Set: is a collection which is unordered, un-indexed and unmodifiable, but we can add new items to the set. Duplicate members are not allowed.
Dictionary: is a collection which is unordered, changeable(modifiable) and indexed. No duplicate members.
 """
 
# 1. Convert the ages to a set and compare the length of the list and the set, which one is bigger?
print(f'list age = {age}\n')
st = set(age)
print(f'set st = {st}\n')
print(f'Compare the length of the list(age) and the set(st) : {len(age)} = {len(st)} => {len(age) == len(st)}\n')

# 1. Explain the difference between the following data types: string, list, tuple and set
print('There are four collection data types in Python :\n ' + 
'String : Text is a string data type. Any data type written as text is a string. Any data under single, double or triple quote are strings. \n ' +
'List: is a collection which is ordered and changeable(modifiable). Allows duplicate members.\n ' + 
'Tuple: is a collection which is ordered and unchangeable or unmodifiable(immutable). Allows duplicate members. \n Set: is a collection which is unordered, un-indexed and unmodifiable, but we can add new items to the set. Duplicate members are not allowed.\n')

# 2. _I am a teacher and I love to inspire and teach people._ 
# How many unique words have been used in the sentence? 
# Use the split methods and set to get the unique words.
phrase = "I am a teacher and I love to inspire and teach people"
print(f'Phrase : \n {phrase} \n')
words = phrase.split()
print(f'All words : length({len(words)}) \n {words}\n ')
unique_words = set(words)
print(f'Unique words : length({len(unique_words)}) \n {unique_words} \n')