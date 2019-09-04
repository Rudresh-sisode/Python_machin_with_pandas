#Do data manipulation and which day got maximum calls foe ems and how many
import pandas as pd
df=pd.read_csv('911.csv')
type(df['timeStamp'].iloc[0])
df['timeStamp']=pd.to_datetime(df['timeStamp'])
df['Day of Week']=df['timeStamp'].apply(lambda time: time.dayofweek)
dmap={0:'mon',1:'tue',2:'wed',3:'thu',4:'fri',5:'Sat',6:'sum'}
df['Day of Week']=df['Day of Week'].map(dmap)
df['Reason']=df['title'].apply(lambda title:title.split(':')[0])
p=df['Reason'].value_counts()
f=df[df['Reason']=='EMS'].max()
print(f)
