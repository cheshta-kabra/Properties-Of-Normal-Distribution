import random
import plotly.figure_factory as ff 
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import statistics 

df=pd.read_csv('StudentsPerformance.csv')
mathList=df['math score'].to_list()
mean=sum(mathList)/len(mathList)
std_dev=statistics.stdev(mathList)
median=statistics.median(mathList)
mode=statistics.mode(mathList)
print ("Mean",mean)
print ("Median",median)
print ("Mode",mode)
print ("Std_Dev",std_dev)
""" fig=px.bar(x=mathList,y=count)
fig.show() """
print (len(mathList))
FStd_devStart,FStd_DevEnd=mean-std_dev,mean+std_dev
SStd_devStart,SStd_DevEnd=mean-(std_dev*2),mean+(std_dev*2)
TStd_devStart,TStd_DevEnd=mean-(std_dev*3),mean+(std_dev*3)
fig=ff.create_distplot([mathList],['Result'],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode='lines',name='MEAN'))
fig.add_trace(go.Scatter(x=[FStd_devStart,FStd_devStart],y=[0,0.17],mode='lines',name='Std_dev1'))
fig.add_trace(go.Scatter(x=[FStd_DevEnd,FStd_DevEnd],y=[0,0.17],mode='lines',name='Std_dev1'))
fig.add_trace(go.Scatter(x=[SStd_devStart,SStd_devStart],y=[0,0.17],mode='lines',name='Std_dev2'))
fig.add_trace(go.Scatter(x=[SStd_DevEnd,SStd_DevEnd],y=[0,0.17],mode='lines',name='Std_dev2'))
fig.show()
listOfDataIn1Std_dev=[result for result in mathList if result>FStd_devStart and result<FStd_DevEnd]
listOfDataIn2Std_dev=[result for result in mathList if result>SStd_devStart and result<SStd_DevEnd]
listOfDataIn3Std_dev=[result for result in mathList if result>TStd_devStart and result<TStd_DevEnd]
print('Percentages of Data In 1st Std_dev',len(listOfDataIn1Std_dev)/len(mathList)*100)
print('Percentages of Data In 2st Std_dev',len(listOfDataIn2Std_dev)/len(mathList)*100)
print('Percentages of Data In 3st Std_dev',len(listOfDataIn3Std_dev)/len(mathList)*100)
