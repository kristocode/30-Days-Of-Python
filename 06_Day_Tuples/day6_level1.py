## 💻 Exercises: Day 6

### Exercises: Level 1

# 1. Create an empty tuple
my_tuple = tuple()
# 2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
sisters = ('Janis Joplin', 'Amy Winehouse')
brothers = ('Brian Jones', 'Jimi Hendrix', 'Jim Morrison', 'Kurt Cobain')
# 3. Join brothers and sisters tuples and assign it to siblings
club_27 = brothers + sisters
# 4. How many siblings do you have?
print(f'I have {len(club_27)} siblings\n')
# 5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = list(club_27)
family_members.append('father_name')
family_members.append('mather_name')
club_27 = tuple(family_members)

print(f'Added father and mather : {club_27}\n')