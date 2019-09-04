#What are the top 4 townships for 911 calls and which are not present given below
#Lwer Pottsgrove, Norristown,HOrsham,Abington
import pandas as pd
df=pd.read_csv('911.csv')
p=df['twp'].value_counts().head(4)
q=('LOWER POTTSGROVE','NORRISTOWN','HORSHAM','ABINGTON')
h=('LOWER POTTSGROVE','HORSHAM')
if q not in p:
    print(h)
elif q in p:
    print(p)
else:
    print('it\'s here')
