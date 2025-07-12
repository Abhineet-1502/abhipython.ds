import pandas as pd
data={
    'Name':['Abhineet','Manashi','Aliester','mitchell','Dhoni'],
    'Age':[20,21,23,40,42],
    'City':['New York','Las Vegas','Los Angelas','Amsterdam','Ranchi']
}
df=pd.DataFrame(data)
print(df)
csv_file='Data.csv'
df.to_csv(csv_file, index='False')