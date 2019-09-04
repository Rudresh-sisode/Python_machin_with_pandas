#Plot barchart using matplot for 911 calls by reason and how can
#you plot the bars horizintally?
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
df=pd.read_csv('911.csv')
df1=df['title'].apply(lambda title:title.split(':')[0])
p=df1.value_counts()
h=sns.countplot(y=df1)
plt.show(h)
print(p)
