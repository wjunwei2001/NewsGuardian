import pandas as pd

true = pd.read_csv('True.csv')
fake = pd.read_csv('Fake.csv')
true['label'] = 1
fake['label'] = 0
frames = [true.loc[:][:], fake.loc[:][:]]
df = pd.concat(frames)

X = df.drop('label', axis=1) 
y = df['label']
df = df.dropna()
df2 = df.copy()
df2 = df2.reset_index(drop = True)
df.describe()

