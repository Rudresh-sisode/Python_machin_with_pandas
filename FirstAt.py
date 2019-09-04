#What are the top 10 zipcode for 911, are zipcodes 19446 and 19090 present?
import pandas as pd
df=pd.read_csv('911.csv')
p=df['zip'].value_counts().head(10);
print(p)
if all((any(df['zip']==19446),any(df['zip']==19090))):
    print('yes')
else:
    print('no')
