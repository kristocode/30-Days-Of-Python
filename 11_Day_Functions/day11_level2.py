## 💻 Exercises: Day 11

### Exercises: Level 2

#1.  Declare a function named evens_and_odds . 
# It takes a positive integer as parameter and it counts number of evens and odds in the number.

'''py
    print(evens_and_odds(100))
    # The number of odds are 50.
    # The number of evens are 51.
'''
def evens_and_odds(nro):
    odds = 0 
    evens = 0
    for i in range(nro+1):   
           
        if(i % 2 == 0): # if is even  
            
            evens += 1
        else:
              
            odds += 1
    return f"The number of odds are {odds}\nThe number of evens are {evens}"
    

print(evens_and_odds(100), '\n')
# 1. Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number

def factorial(number):
    fact = 1
    for i in range(1,number+1):        
        fact *= i
    return fact

print(factorial(26))

def factorial_rec(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * factorial_rec(number-1)

print(factorial_rec(26), '\n')

# 1. Call your function _is_empty_, it takes a parameter and it checks if it is empty or not

def is_empty(*params):
    if len(params):
        return True
    return False
print('Arguments are passed to the function ' if is_empty(0,'arg1', 9.8) else 'No arguments passed to the function \n')
print('Arguments are passed to the function ' if is_empty() else 'No arguments passed to the function  \n')

# 1. Write different functions which take lists. 
# They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, 
# calculate_std (standard deviation).

def calculate_mean(lst):    #averange
    return sum(lst)/len(lst)
#print(calculate_mean([5,5]))

def calculate_median(lst):
    middle = (len(lst)-1)//2
    median = 0
    if (len(lst)%2 == 0) : # pair
        median = (lst[middle] + lst[middle+1]) / 2
    else :
        median = lst[middle] 
    return median
#print(calculate_median([5,5,4,6]))

def calculate_mode(lst):    
    cnt = lst.count(lst[0])
    #print('cnt : ',cnt, ' lst[0] : ', lst[0])
    mode = [lst[0]]
    for i in range(1, len(lst)):
        #print('cnt : ',lst.count(lst[i]), ' lst[i] : ', lst[i])
        if (cnt <= lst.count(lst[i])) and (lst[i] not in mode):
            cnt = lst.count(lst[i])
            mode.append(lst[i])        

    return mode

def calculate_range(lst):    
    return max(lst) - min(lst)
#print(calculate_range([5,5,4,6]),'\n')

def calculate_variance(lst):
    sum = 0
    mu = calculate_mean(lst)
    for i in lst:
        sum += (i-mu)**2
    return sum/len(lst)

def calculate_std(lst): #(standard deviation)    
    return (calculate_variance(lst))**0.5

def calculate_function(f, lst):
    if not lst:
        return 'Empty list'
    return f(lst)

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 19,24]
print('Mean : ', calculate_function(calculate_mean, []))
print('Mean : ',calculate_function(calculate_mean, ages),'\n')
print('Median : ',calculate_function(calculate_median, []))
print('Median : ',calculate_function(calculate_median, ages), '\n')
print('Mode : ',calculate_function(calculate_mode, ages), '\n')
print('Range : ',calculate_function(calculate_range, ages), '\n')
print('Variance : ',calculate_function(calculate_variance, ages), '\n')
print('Standar Deviation : ',calculate_function(calculate_std, ages), '\n')
