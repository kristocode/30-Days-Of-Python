# 1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
print('#1 : ')
space = ' '
phrase = 'Thirty' + space + 'Days' +  space + 'Of' + space +  'Python'
print(phrase)
# 2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
print('#2 : ')
phrase2 = 'Coding' + space +  'For' + space + 'All'
print(phrase2)
# 3. Declare a variable named company and assign it to an initial value "Coding For All".
print('#3 : ')
company = phrase2
# 4. Print the variable company using _print()_.
print('#4 : ')
print(company)
# 5. Print the length of the company string using _len()_ method and _print()_.
print('#5 : ')
print('Length of the variable company : ', len(company))
# 6. Change all the characters to uppercase letters using _upper()_ method.
print('#6 : ')
print('Change all the characters to uppercase of the variable company : ', company.upper())
# 7. Change all the characters to lowercase letters using _lower()_ method.
print('#7 : ')
print('Change all the characters to lowercase of the variable company : ', company.lower())
# 8. Use capitalize(), title(), swapcase() methods to format the value of the string _Coding For All_.
print('#8 : ')
print('Used capitalize() in the variable company : ', company.capitalize())
print('Used title() in the variable company : ', company.title())
print('Used swapcase() in the variable company : ', company.swapcase())
# 9. Cut(slice) out the first word of _Coding For All_ string.
print('#9 : ')
print(company[0 : 6])
print(company[0 : int(len('Coding'))])
print(company[0 : company.find(' ')])
# 10. Check if _Coding For All_ string contains a word Coding using the method index, find or other methods.
print('#10 : ')
word = 'Coding'
print(company.find(word) != -1)
print(company.index(word)) #If is error return => ValueError: substring not found
# 11. Replace the word coding in the string 'Coding For All' to Python.
print('#11 : ')
word2 = 'Python'
phrase3 = company.replace(word, word2)
print(phrase3) # Python For All
# 12. Change 'Python for Everyone' to 'Python for All' using the replace method or other methods.
print('#12 : ')
phrase4 = 'Python for Everyone'
print(phrase4.replace('Everyone', 'All'))
# 13. Split the string 'Coding For All' using space as the separator (split()) .
print('#13 : ')
print(company.split())
# 14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
print('#14 : ')
phrase5 = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(phrase5.split(', '))
# 15. What is the character at index 0 in the string _Coding For All_.
print('#15 : ')
print(company[0])
# 16. What is the last index of the string _Coding For All_.
print('#16 : ')
print(len(company)-1)
# 17. What character is at index 10 in "Coding For All" string.
print('#17 : ')
print(company[10])
# 18. Create an acronym or an abbreviation for the name 'Python For Everyone'.
print('#18 : ')
acronym = phrase4.title().split()
print(f'{acronym[0][0:1]}{acronym[1][0:1]}{acronym[2][0:1]}')
# 19. Create an acronym or an abbreviation for the name 'Coding For All'.
print('#19 : ')
acronym = phrase2.split()
print(f'{acronym[0][::3]}{acronym[1][::3]}{acronym[2][::3]}')
# 20. Use index to determine the position of the first occurrence of C in Coding For All.
print('#20 : ')
print(phrase2.index('C'))
# 21. Use index to determine the position of the first occurrence of F in Coding For All.
print('#21 : ')
print(phrase2.index('F'))
# 22. Use rfind to determine the position of the last occurrence of l in Coding For All People.
print('#22 : ')
phrase2 += space + 'People'
print(phrase2.rfind('l'))
# 23. Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
print('#23 : ',sentence.find('because'))
print('#23 : ',sentence.index('because'))
# 24. Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print('#24 : ',sentence.rindex('because'))
print('#24 : ',sentence.rfind('because'))
# 25. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
substr = 'because'
print('#25 : ',sentence[0:sentence.index(substr)] + sentence[sentence.rfind(substr)+len(substr)+1:])
print('#25 : ',sentence.replace('because ', ''))
# 26. Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# idem 23
# 27. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# idem 25
# 28. Does '\'Coding For All' start with a substring _Coding_?
print('#28 : ', phrase2.startswith('Coding'))
# 29. Does 'Coding For All' end with a substring _coding_?
print('#29 : ', phrase2.endswith('Coding'))
# 30. '&nbsp;&nbsp; Coding For All &nbsp;&nbsp;&nbsp; &nbsp;' &nbsp;, remove the left and right trailing spaces in the given string.
nbsp = '   Coding For All      '
print('#30 : ',nbsp.strip())
# 31. Which one of the following variables return True when we use the method isidentifier():
    #- 30DaysOfPython
id = '30DaysOfPython'
print('#31 : ',id.isidentifier())     
    #- thirty_days_of_python
id = 'thirty_days_of_python'
print('#31 : ',id.isidentifier())     
# 32. The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('#32 : ',' '.join(libraries))
# 33. Use the new line escape sequence to separate the following sentences.
""" py
I am enjoying this challenge.
I just wonder what is next.
    """
print('#33 : ')
print('I am enjoying this challenge.\nI just wonder what is next.')
# 34. Use a tab escape sequence to write the following lines.
'''py
Name      Age     Country   City
Asabeneh  250     Finland   Helsinki
'''
print('#34 : ')
print('Name    \tAge\tCountry \tCity')
print('Asabeneh\t250\tFinland \tHelsinki')
# 35. Use the string formatting method to display the following:
'''sh
radius = 10
area = 3.14 * radius ** 2
The area of a circle with radius 10 is 314 meters square.
'''
print('#35 : ')
radius = 10
area = 3.14 * radius ** 2
print(f'The area of a circle with radius {radius} is {area:.0f} meters square.')
# 36. Make the following using string formatting methods:

'''sh
8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144
'''
print('#36 : ')
a=8
b=6
print(f'{a} + {b} = {a+b}')
print(f'{a} - {b} = {a-b}')
print(f'{a} * {b} = {a*b}')
print(f'{a} / {b} = {a/b:.2f}')
print(f'{a} % {b} = {a%b}')
print(f'{a} // {b} = {a//b}')
print(f'{a} ** {b} = {a**b}')
