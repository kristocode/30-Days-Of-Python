### Exercises: Level 2

# 1. Unpack siblings and parents from family_members
family_members = ('Brian Jones', 'Jimi Hendrix', 'Jim Morrison', 'Kurt Cobain', 'Janis Joplin', 'Amy Winehouse', 'father_name', 'mather_name')
print(f'family_members : \n{family_members}\n')
family_members = list(family_members)
*family_members, father, mather = family_members
family_members = tuple(family_members)
print(f'Unpack siblings and parents from family_members : \n {family_members}\n')
#family_members.reverse() 
#mather, father, *club_27 = family_members

# 1. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('banana', 'orange', 'apple', 'kiwi')
vegetables = ('potato', 'onion', 'pepper', 'carrot')
products = ('herb', 'rice', 'noddles', 'salt')
food_stuff_tp = fruits + vegetables + products
print(f'food_stuff_tp {food_stuff_tp}\n')

# 1. Change the about food_stuff_tp  tuple to a food_stuff_lt list
food_stuff_lt =list(food_stuff_tp)
print(f'food_stuff_lt : {food_stuff_lt} => type : {type(food_stuff_lt)}\n')

# 1. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle = (len(food_stuff_tp)-1)//2
if (len(food_stuff_tp)%2 != 0) :
  print(f'food_stuff_tp is odd and show the middle item : {food_stuff_tp[middle]} \n')
else : 
  print(f'food_stuff_tp is pair and show the middle items : {food_stuff_tp[middle:middle+2]} \n')

# 1. Slice out the first three items and the last three items from food_staff_lt list
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]
print(f'First three items : {first_three}')
print(f'Last three items : {last_three}\n')

# 1. Delete the food_staff_tp tuple completely
del food_stuff_tp

# 1. Check if an item exists in  tuple:
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print(f"Exist item ({'Argentina'}) in tuple {nordic_countries}? : {'Argentina' in nordic_countries}\n")
print(f'')
# - Check if 'Estonia' is a nordic country
print(f"Check if  ({'Estonia'}) is a nordic country : {'Estonia' in nordic_countries}\n")

# - Check if 'Iceland' is a nordic country
print(f"Check if  ({'Iceland'}) is a nordic country {nordic_countries}? : {'Iceland' in nordic_countries}\n")
'''py
  nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
'''
