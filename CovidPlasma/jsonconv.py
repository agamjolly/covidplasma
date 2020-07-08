import pandas as pd

df = pd.read_csv('./covidList.csv')
#df.set_index('id',inplace=True)
df.to_json('./cov.json',orient='records')
