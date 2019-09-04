import pandas as pd
file=pd.read_csv('911.csv')
file.dropna();
top_zip=file[file['twp']]['zip'].value_count().head(10)
print(top_zip)
