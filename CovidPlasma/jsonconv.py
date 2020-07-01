import pandas as pd

df = pd.read_csv('./covidListFile.csv')
df.set_index('id',inplace=True)
df.to_json('./cov.json')
