import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv('olympics.csv', skiprows=4)

m=data[(data.Edition==2008)&(data.NOC =='CHN')]
m.Gender.value_counts()
#m.Gender.value_counts().plot(kind='bar')

sns.countplot(data=m,x='Gender')

sns.countplot(x='Medal',data=m,hue='Gender')