## 💻 Exercises: Day 10

### Exercises: Level 1

# 1. Iterate 0 to 10 using for loop, do the same using while loop.
print("#1")

print('nro : ', end='')
for nro in range(11):    
    print(nro, end=" - ") if (nro<10) else print(nro)

co = 0
print('co : ', end='')
while co < 11:
    print(co, end=" - ") if (co<10) else print(co)
    co += 1

# 2. Iterate 10 to 0 using for loop, do the same using while loop.
print("#2")
print('nro_i : ', end='')
for nro_i in range(10,-1,-1):    
    print(nro_i, end=" - ") if (nro_i>0) else print(nro_i)

co_i = 10
print('co_i : ', end='')
while co_i >= 0:
    print(co_i, end=" - ") if (co_i>0) else print(co_i)
    co_i -= 1


# 3. Write a loop that makes seven calls to print(), so we get on the output the following triangle:
print("#3")
'''py
     #
     ##
     ###
     ####
     #####
     ######
     #######
'''
for pad in ['#', '##', '###', '####', '#####', '######', '#######']:
    print(pad)

for n in range(1,8):    
    for i in range(1,n+1):        
        print("#", end="") if(i<n) else print("#", end="\n")

cad=""
for n in range(1,8):    
    for i in range(1,n+1):        
        cad += (("#") if(i<n) else ("#\n"))
print(cad)

# 4. Use nested loops to create the following:
print("#4")
'''sh
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
'''
for i in range(8):
    for j in range(8):
        print("# ", end="") if(j<7) else print("#", end="\n")
    
# 5. Print the following pattern:
print("#5")
'''sh
0 x 0 = 0
1 x 1 = 1
2 x 2 = 4
3 x 3 = 9
4 x 4 = 16
5 x 5 = 25
6 x 6 = 36
7 x 7 = 49
8 x 8 = 64
9 x 9 = 81
10 x 10 = 100
'''
for i in range(11):
    print(i, ' x ', i, ' = ', i*i, ('' if(i<10) else '\n'))
    
# 6. Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
print("#6")
for item in ['Python', 'Numpy','Pandas','Django', 'Flask']:
    print(item+' ',  end='')
print('\n')

# 7. Use for loop to iterate from 0 to 100 and print only even numbers
print("#7")
for i in range(101):
    print(i, end="") if(i%2 == 0) else print(" ", end="")
print('\n')

# 8. Use for loop to iterate from 0 to 100 and print only odd numbers
print("#8")
for i in range(101):
    print(i, end="") if(i%2 != 0) else print(" ", end="")
print('\n')