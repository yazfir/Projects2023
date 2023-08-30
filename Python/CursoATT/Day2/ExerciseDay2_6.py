import pandas as pd

df = pd.read_csv('Productos.csv', nrows=10000)

#print(df)
#print()
#print( type(df.head(1)) )
print( df.head() )
for x in df.head(2):
    print(x)