import pandas as pd
import numpy as np

modular = []
decimas =[]
for i in range(1,5,1):
    modular.append(i)
    decimas.append(i+10)

print(modular)
print(decimas)

df = pd.DataFrame(list(zip(modular,decimas)), columns = ['Modular','Decimas'])
print(df)

df.to_csv('test.csv', index=False)