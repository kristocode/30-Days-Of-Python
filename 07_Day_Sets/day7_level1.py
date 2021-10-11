## 💻 Exercises: Day 7


# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]


### Exercises: Level 1
print(f'Set it_companies : \n {it_companies} \n')

# 1. Find the length of the set it_companies
print(f'Length of the set it_companies : {len(it_companies)} \n')

# 2. Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(f"Add 'Twitter' to it_companies : {it_companies} \n")

# 3. Insert multiple IT companies at once to the set it_companies
it_companies.update(['Solar City', 'SpaceX', 'Tesla'])
print(f"Add 'Twitter' to it_companies : {it_companies} \n")

# 4. Remove one of the companies from the set it_companies
it_companies.pop() 
print(f'Remove one of the companies from the set it_companies : {it_companies}\n')

# 5. What is the difference between remove and discard
# remove() method will raise errors
#it_companies.remove('Sun Microsistem') 
print(f'Remove an item using the remove() method - If the item is not found remove() method will raise errors : {it_companies}\n')

# discard() method doesn't raise any errors.
it_companies.discard('Sun Microsistem')
print(f'Remove an item using the discard() method - If the item is not found discard() doesn\'t raise any errors : {it_companies}\n')

