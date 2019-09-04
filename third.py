#create new feature and what is the most common reason for the 911 call based on reason column?
#which column comes second?
import pandas as pd
df=pd.read_csv('911.csv')
p=df['title'].nunique()
df1=df['title'].apply(lambda title: title.split(':')[0])
print(p)
print(df1)
