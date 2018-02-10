import pandas

df = pandas.read_excel("data/supermarkets.xlsx", sheet_name=0)
print(df.drop(df.index[0:3], 0))
