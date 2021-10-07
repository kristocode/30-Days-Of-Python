## 💻 Exercises: Day 5

### Exercises: Level 1

# 1. Declare an empty list
print('#1 : ')
lst = list()
# 2. Declare a list with more than 5 items
print('#2 : ')
lst = list(range(10))
print('List with more than 5 : ', lst)
# 3. Find the length of your list
print('#3 : ')
print('Length of the list : ', len(lst))
# 4. Get the first item, the middle item and the last item of the list
print('#4 : ')
print(f'First item : {lst[0]}\nMiddle item : {lst[len(lst)//2]}\nLast item : {lst[len(lst)-1]}')
# 5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
print('#5 : ')
mixed_data_types = ['Elon', 50, 1.78, False, 'Address']
print(f'mixed_date_types : {mixed_data_types}')
# 6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
print('#6 : ')
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
# 7. Print the list using _print()_
print('#7 : ')
print(f'it_companies : {it_companies}')
# 8. Print the number of companies in the list
print('#8 : ')
print(f'Number of companies in the it_companies : {len(it_companies)}')
# 9. Print the first, middle and last company
print('#9 : ')
print(f'First item : {it_companies[0]}')
print(f'Middle item : {it_companies[len(it_companies)//2]}\nLast item : {it_companies[len(it_companies)-1]}')
# 10. Print the list after modifying one of the companies
print('#10 : ')
it_companies[len(it_companies)-1] = 'Amazonias'
print(f'Modifying last item : {it_companies}')
# 11. Add an IT company to it_companies
print('#11 : ')
it_companies.append('SpaceX')
print(f"Add item : {it_companies}")
# 12. Insert an IT company in the middle of the companies list
print('#12 : ')
it_companies.insert(len(it_companies)//2 ,'Blue Origin')
print(f"Insert item : {it_companies}")
# 13. Change one of the it_companies names to uppercase (IBM excluded!)
print('#13 : ')
print('it_companies[0] names to uppercase : ', it_companies[0].upper())
# 14. Join the it_companies with a string '#;&nbsp; '
print('#14 : ')
print('# '.join(it_companies))
# 15. Check if a certain company exists in the it_companies list.
print('#15 : ')
print('Exists company IBM in it_companies? ', 'IBM' in it_companies)
# 16. Sort the list using sort() method
print('#16 : ')
it_companies.sort()
print(f'Sort the list : {it_companies}')
# 17. Reverse the list in descending order using reverse() method
print('#17 : ')
it_companies.sort(reverse=True)
print(f'Sort the list in descending order : {it_companies}')
# 18. Slice out the first 3 companies from the list
print('#18 : ')
print('Slice out the first 3 companies from the list : ', it_companies[0:3])
# 19. Slice out the last 3 companies from the list
print('#19 : ')
print('Slice out the last 3 companies from the list : ', it_companies[-3:])
print(it_companies)
# 20. Slice out the middle IT company or companies from the list
print('#20 : ')
middle = (len(it_companies)-1)//2 
print(f'Slice out the middle IT company or companies from the list {it_companies[middle]}') if (len(it_companies)%2 != 0) else print(f'Slice out the middle IT company or companies from the list {it_companies[middle:middle+2]}')
print(it_companies)

# 21. Remove the first IT company from the list
print('#21 : ')
print(f"Remove the first IT company '{it_companies[0]}' from the list : \n{it_companies}" )
it_companies.pop(0)
print(it_companies,'\n')

# 22. Remove the middle IT company or companies from the list
print('#22 : ')
middle = (len(it_companies)-1)//2
print(len(it_companies)%2)
if (len(it_companies)%2 != 0) :
    print(f'Remove the middle IT company {it_companies[middle]} from the list : ' )
    it_companies.pop(middle)
else :
    print(f'Remove the middle IT companies {it_companies[middle:middle+2]} from the list : ' )
    del it_companies[middle:middle+2]
print(it_companies)

# 23. Remove the last IT company from the list
print('#23 : ')
last = len(it_companies)-1
print(f"Remove the first IT company '{it_companies[last]}' from the list : {it_companies.pop(last)}" )
print(it_companies)
# 24. Remove all IT companies from the list
print('#24 : ')
print(f'Remove all IT companies from the list : {it_companies.clear()}')
print(it_companies)
# 25. Destroy the IT companies list
print('#25 : ')
print(f'Destroy the IT companies list :')
#del it_companies
print(it_companies)

# 26. Join the following lists:
print('#26 : ')
'''py
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
'''
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
join_lists = front_end + back_end
print(f'Join the lists front_end and back_end : {join_lists}')
# 27. After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
print('#27 : ')
full_stack = join_lists.copy()
full_stack.extend(['Python', 'SQL', 'Redux'])
print(full_stack)

