### Exercises: Level 2
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

# 1. Join A and B
AUB = A.union(B)
print(f'Join A and B : {AUB} \n')

# 1. Find A intersection B
AIB = A.intersection(B)
print(f'Find A intersection B : {AIB} \n')

# 1. Is A subset of B
AissubsetB = A.issubset(B)
print(f'Is A subset of B? : {AissubsetB} \n')

# 1. Are A and B disjoint sets
AdisjointB = A.isdisjoint(B)
print(f'Are A and B disjoint sets? : {AdisjointB} \n')


# 1. Join A with B and B with A
A.update(B)
print(f'B contents are added to A:\n A = {A}\n')

B.update(A)
print(f'A contents are added to B:\n B = {B}\n')

# 1. What is the symmetric difference between A and B
print(f'A : {A} \n')
print(f'B : {B} \n')
#A.symmetric_difference(B)
print(f'Symetric difference between A and B : {A.symmetric_difference(B)}')

# 1. Delete the sets completely
del A
del B
#print(f'A : {A} \n') #NameError: name 'A' is not defined
#print(f'B : {B} \n') #NameError: name 'B' is not defined