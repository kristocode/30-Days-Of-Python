'''Exercise: Level 3
Write an example for different Python data types such as Number
(Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary.
'''
print('Data types')
print('Integer : ', type(26))          # Int
print('Float : ', type(2.718281828))        # Float
print('Complex : ', type(6j))      # Complex number
print('String : ', type('This is a string'))  # String
print('List : ', type(['Apple', 3.14, True, [1, '5']]))   # List
print('Dictionary : ', type({'day': '01', 'mounth' : 'January', 'year' : '2021', 'number' : 4})) # Dictionary
print(type({20.5, 5.2, 2.7, 'string', False}))    # Set
print(type((9.8, 30, 'tuple', True)))    # Tuple

'''Find an Euclidian distance between (2, 3) and (10, 8)'''
p1 = {'x' : 2, 'y' : 3}
p2 = {'x' : 10, 'y' : 8}
dE = ((p2['x'] - p1['x']) + (p2['y']- p1['y']))** 0.5
print('Euclidian distance between (2, 3) and (10, 8) : ', dE)