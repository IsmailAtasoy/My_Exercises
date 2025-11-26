import numpy as np
from numpy import random

#SEARCHING
'''
arr = np.array([0,10,20,30,0,40,50,50,60,70])
arr2 = np.array([0,10,20])

result = np.where(arr==50) #gives the index no
result2 = np.where(arr>30) #gives the index no
result3 = np.isin(arr,arr2) #compare if arr2 is in arr (bool)
result4 = np.nonzero(arr)  #gives index of nonzero items
result5 = np.argmin(arr) #gives the min value items index
result6 = np.argmax(arr) #gives the max value items index
result7 = np.searchsorted(arr,40) #gives the appropriate index to add the value sorting from left 

print(result)
print(result2)
print(result3)
print(result4)
print(result5)
print(result6)
print(result7)

'''

#SORTING
'''
arr = np.array([6,2,7,4,3,8,10])
names = np.array(["james","daniel","james","levin"])
scores = np.array([100,50,45,60])
arr2d = np.array([[1,6,5,9], [5,2,4,10]])

result = np.sort(arr) #sort the array lower to higher. Also we can sort strings.
result2 = np.sort(arr2d,axis=0) #sort array for coulumns. Also no axis parameter for rows.
result3 = np.argsort(arr) #sort array and write the indexes
result4 = np.lexsort((scores,names)) #if names are same order by scores.

print(result)
print(result2)
print(result3)
print(list(zip(names[result4],scores[result4])))
'''

#FILTER
'''
arr = np.array([10,20,30,40,50])
filter_arr = arr[[True,False,False,True,True]] #write only True items

filter_arr2 = []
for item in arr:
    if item > 30:
        filter_arr2.append(True)
    else:                           #we are creating a filter here with for and if condition
        filter_arr2.append(False) 
new_arr = arr[filter_arr2]
print(filter_arr2)
print(new_arr)

simple_filter = arr > 30
new_arr2 = arr[simple_filter]       #its shorter than above
print(simple_filter)
print(new_arr)
'''

#RANDOM ARRAYS
"""
result1 = random.randint(100) #generate random integer from 0 to 99
result2 = random.rand() #generate random float between 0 and 1
result3 = random.randint(100,size=(3,3)) #generate 3x3 matrix with random integers
result4 = random.rand(5) #generate 5 items array random floats, or we can create matrix as above
#random.seed(1000) if we use seed always takes same random numbers from functions

arr = [10,20,30,40,50,60,70,80,90]
result5 = random.choice(arr,size=(4,3)) #generate a 4x3 matrix by array items randomly

print(result5)
"""

#RANDOM DATA DISTRIBUTION
'''
arr = [1,2,3,4,5,6]

result = random.choice(arr,p=[0.5,0.2,0.1,0.1,0.1,0.0],size=100) #decide probability of items 

#values,counts = np.unique(result,return_counts=True)    
#for val,count in zip(values,counts):
    #print(f"{val} : {count} times seen")

result2 = random.permutation(arr) #copy shuffle
random.shuffle(arr) #shuffle original array
'''

