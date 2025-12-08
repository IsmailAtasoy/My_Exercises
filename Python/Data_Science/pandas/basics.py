import pandas as pd
import numpy as np

#Series 
'''
numbers = [1,2,3,4]
names = ["Jack","Liss","Mia","Paul"]
combined = [1,2,3.42,"Lissens","Cole","Dann",True,False]

result1 = pd.Series(numbers)
result2 = pd.Series(names)
result3 = pd.Series(combined)
result4 = pd.Series(numbers,index=["a","b","c","d"]) #we can return items with index numbers and renamed them

print(result1)
'''

#Special Index Name
'''
MyData = list(range(1,101))
MyIndex = [f"a{i}" for i in range(1,101)]
result = pd.Series(MyData,index=MyIndex)

print(result)
'''

#Dictionary Usage
'''
calories = {"day1":420,"day2":347,"day3":572}
result = pd.Series(calories)
print(result)
'''

#Dataframe
'''
MyData = [

    ["Jack",23],
    ["Souttar",18],
    ["Will",56]
]

result = pd.DataFrame(MyData,index=[1,2,3],columns=["Name","Age"])
print(result)
'''

'''
MyData = {

    "Name":["Jack","Souttar","Will"],
    "Age":[23,18,56],
    "Country":["Usa","Scotland","Wales"]
}

result = pd.DataFrame(MyData,index=[1,2,3])
print(result)
'''

'''
MyData = {
    "Name":[f"Name{i}" for i in range(1,51)],
    "Age":[i for i in np.random.randint(100,size=50)+1],
    "Country":[f"Country{i}" for i in range(1,51)]
}
Index = [i for i in range(1,51)]
result = pd.DataFrame(MyData,index=Index)
print(result.head(10)) #return first 10 data
print(result.tail(10)) #return last 10 data
print(result.loc[[1,10,20]]) #return 1. 10. 20. data
'''

'''
MyData = {

    "product":["ball","shoe","umbrella","t-shirt"],
    "amount":[20,50,40,30],
    "price":[5,45,20,15]
}

result = pd.DataFrame(MyData)
result["income"] = result["amount"] * result["price"]
print(result)
'''


