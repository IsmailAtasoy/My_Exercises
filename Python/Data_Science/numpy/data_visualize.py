import matplotlib.pyplot as plt
import seaborn as sb
import numpy as np

#sb.displot([0,1,2,3,4,2,2,2,2,2,3,3,3,4,4]) #distribution plot

notes = [50,30,50,50,45,20,25,20,35,60,65]
data = np.array([[10,20],[30,40]])

#sb.displot(notes,kind='kde')
#sb.histplot(notes,bins=10)
#sb.kdeplot(notes)
#sb.ecdfplot(notes)
#sb.lineplot(x=[1,2,3,8,12],y=[10,30,40,45,50])
#sb.scatterplot(x=[1,2,3,4],y=[4,3,2,1])
#sb.barplot(x=["A","B","C"],y=[5,2,6])
#sb.boxplot(x=[1,2,3,4,5,6,7]) #box the mid
#sb.violinplot(x=[1,2,3,4,5,6,7]) #violin the mid
#sb.heatmap(data) #color the items by their velues
plt.show()