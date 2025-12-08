import pandas as pd
import numpy as np

pd.options.display.max_rows = 200

'''
result1 = pd.read_csv()
result2 = pd.read_excel()
result3 = pd.read_json()
print(result1.to_string())
'''

"""
data = pd.read_csv("stats.csv")

goals = data[["team","goals","season"]]
print(goals[goals["goals"]>70])
"""

'''
data = pd.read_csv("stats.csv")
result = data.dropna() #if there are empty datas delete the row
print(result.to_string())
result2 = data.dropna(inplace=True) #change original data
print(data.to_string())
result3 = data.fillna(100,inplace=True) #fill the empty datas with 100
'''

'''
data = pd.read_csv("data.csv")
data["Date"] = pd.to_datetime(data["Date"],format="mixed")
print(data.to_string())
data.dropna(subset=["Date"],inplace=True)
'''








