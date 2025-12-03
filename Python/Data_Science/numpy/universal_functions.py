import numpy as np

#Arithmetic Operators
'''
x = np.array([4,5,6,7])
y = np.array([2,5,2,6])

result = np.add(x,y) 
result2 = np.subtract(x,y)
result3 = np.true_divide(x,y) #exact value
result4 = np.floor_divide(x,y) #integer value
result5 = np.divide(x,y) #floating value
result6 = np.power(x,y) #x**y
result7 = np.float_power(x,y) 
result8 = np.mod(x,y) #x % y
result9 = np.square(x) #x**2
result10 = np.sqrt(x) # x**(1/2)
result11 = np.floor(5.2) #round the floor
result12 = np.ceil(-3.4) #round the ceil

result13 = np.exp(1) #e**x the formula
result14 = np.exp2(2) #2**x the formula
result15 = np.expm1(2) #e**x - 1

#You can access many operator like this on numpy and these are faster than pythons own tools.

print(result11)
'''

#Add Your Function to Universal Function
'''
def My_Func(x,y):
    return x+y

myAdd = np.frompyfunc(My_Func,2,1) #2 input 1 output
print(type(myAdd))
'''

#Controls
'''
c1 = np.isnan(np.nan) #if not number return True
c2 = np.isinf(np.inf) #return True
c3 = np.isfinite(np.inf) #return False
c4 = np.isreal(7+0j)
c5 = np.iscomplex(7+1j)
'''





















