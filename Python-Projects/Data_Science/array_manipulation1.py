import numpy as np

#ARRAYS

arr0 = np.array(10) #0d array

arr1 = np.array([10,20,30,40]) #1d array

arr2 = np.array([[10,20,30],
                 [40,50,60]
                 ]) #2d array

arr3 = np.array([
            [
                  [10,20,30],
                  [40,50,60]
            ], 
            [
                  [70,80,90],
                  [100,110,120]
            ]
]) #3d array

# arr.ndim for see the dimension of array
# np.arange(x,y,1) for creating array starts with x ends with y-1 
# np.linspace(x,y,z) for creating array that divided to z equally between x and y
# np.eye(x) for creating x*x identity matrix 
# np.full((x,y),z) for creating x*y matrix that is all items are z
# np.empty((x,y)) for creating x*y matrix that is random valued



#INDEX
'''
print(arr1[0:3],"\n")

print(arr2[1,1],"\n")   #Its like array index 
print(arr2[:,1],"\n")
print(arr2[arr2>20])    #If the data higher than 20 write it

print(arr3[0,0,0])      #First argument for wall second for row third for coulumn
'''


#DATA TYPES
'''
array = np.array([7.22222], dtype=np.float32)
print(array.dtype)
array1 = np.array([True,False])
print(array1.dtype)
array2 = np.array(['hello','world'])
print(array2.dtype)

#Also we can use complex numbers either

new_array = array.astype(bool)
print(new_array)
print(new_array.dtype)
 
#dtype="object" its for use different data types in a same array as integers floats strings etc...
'''


#COPY VİEW SHAPE METHODS

original_array = np.array([10,20,30,40,50,60])
new_array = original_array.copy()   #the changes on original array doesnt affect this copy
view_array = original_array.view()  #the changes on both original and this array affect each other

x = original_array.copy()   #x.base returns none 
y = original_array.view()   #y.base returns same array of original_array

#arr.shape for showing the dimensions of array

reshaped_array = original_array.reshape(2,3,-1)    #Its for reshaping the array as 3d(2d can be implemented) -1 is for autocomplete the array

#arr.flatten() its converts to 1d an array its a copy array
#arr.ravel() its converts to 1d an array its a view array

#np.flip(arr,axis=0) reverse the rows axis=1 for coulumns
#np.flipud(arr) reverse the rows
#np.fliplr(arr) reverse the coulumns
#arr.T for transpose the matrix



#LOOPS

'''
We can access items by for loops on arrays
If array is 2d or 3d we have to use nested for loop 
We can use np.nditer(arr) for all dimension arrays

for arr_index,arr_value in np.ndenumarate(arr):
      print(arr_index,arr_value)

its output indexes of array
'''


#UNION
'''
x = np.array([[10,20], [30,40]])
y = np.array([[50,60] ,[70,80]])
z = np.concatenate((x,y), axis=1) seperate first arrays and second arrays
if axis=0 write them in order next to down
'''
#np.stack((arr1d,arr1d),axis=0) create a 2d array if axis=1 seperate the coulumns
#np.hstack((arr1d,arr1d)) horizontal array
#np.vstack((arr1d,arr1d)) vertical array
#np.dstack((arr2d,arr2d)) creating 3d array



#SEPERATION
'''
np.array_split(arr,x) split array to x arrays
np.hsplit(arr,x) split 2d array horizontally
np.vsplit(arr,x) split 2d array vertically
np.dsplit(arr,x) split 3d array coulumn by coulumn 
'''