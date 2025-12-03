import matplotlib.pyplot as plt
import seaborn as sb
from numpy import random

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

#NORMAL(GAUSSIAN)
'''
arr = random.normal(loc=20,scale=2,size=100) #local means avarage. scale means standart deviation. 
sb.displot(arr,kind='kde')
plt.title("Normal Distribution")
plt.show()
'''

#Binomial
'''
data = random.binomial(n=10,p=0.5,size=100) # n times try. p is probability of success. 100 person.
sb.displot(data)
plt.title("Binomial Distribution")
plt.show()
#This is for conditions that have 2 results.
'''

#Poisson
'''
data = random.poisson(lam=2,size=100) #lam is avarage. size is like minutes here.
sb.displot(data)
plt.title("Poisson Distribution")
plt.show()
#imagine you have a cafe and you observe how many custemors come per munite.
'''

#Uniform
'''
data = random.uniform(low=0.0,high=10.0,size=100)
sb.displot(data)
plt.title("Uniform Distributoion")
plt.show()
#betwenn two numbers generate random numbers almost equally counts.
'''

#Logistic
'''
data = random.logistic(loc=0.0,scale=1.0,size=100)
sb.histplot(data,kde=True)
plt.title("Logistic Distribution")
plt.show()
#it similiar like normal distribution but at the edges some values rises instead of decreasing.
'''

#Multinomial
'''
data = random.multinomial(n=10,pvals=[1/6]*6)
print(data)
#imagine you have a dice and you diced 10 times and all numbers have same probability.
#also we can add size. it means we try this experiment 10 times on every size of groups.
'''

#Exponential
'''
data = random.exponential(scale=0.5,size=100) #scale = 1/lambda lambda means work on unit time. lambda = 2 in this example.
sb.histplot(data,bins=30,kde=True)
plt.title("Exponential Distribution")
plt.show()
#assume that you are in a bank. while time passing probabilty of new customers decreasing.
'''

#Chi Square
'''
data = random.chisquare(df=5,size=100)
#taking random 5 product and look their scale. sum of squares of scales will be among df value.
print(data)
sb.histplot(data,bins=30,kde=True)
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Chi Square Distribution")
plt.show()
#if value low its good for the product but if it highs it is bad. 
'''

#Rayleigh 
'''
data = random.rayleigh(scale=2.0,size=100)
#scale is like wave height. 
print(data)

sb.histplot(data,bins=30,kde=True)
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Rayleigh Distribution")
plt.show()
'''

#Pareto
'''
xm = 1.0 #start value
data = (random.pareto(2.0,1000)+1)*xm
print(data)

sb.histplot(data,bins=40,kde=True)
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Pareto Distribution (p=2.0)")
plt.show()
#imagine that it is an income if p increases it will be more balanced 
'''

#Zipf
'''
data = random.zipf(2.0,1000)
data = data[10>data]
print(data)

sb.histplot(data,bins=range(1,11),discrete=True)
plt.xlabel("Rank")
plt.ylabel("Frequency")
plt.title("Zipf Distribution (s=2.0)")
plt.show()
#Frequency will decrease continiously. example(60x 30x 20x 15x 12x 10x)  
'''

