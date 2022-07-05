import pandas as pd
import numpy

df = pd.read_csv('Optional-Assignment/exams.csv')

print('Min: ' + str(min(df['writing score'].values)))
print('Max: ' + str(max(df['writing score'].values)))

print('Standard deviation: ' + str(numpy.std(df['reading score'].values)))

df.drop(df.index[2], inplace=True, axis=0)

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
print(df)

print(df.head(5))
print(df.tail(5))

print(df.dtypes)

df['Average '] = df[['math score', 'reading score']].mean(axis=1)


population = df[df['reading score'] < 80]
female_population = population[population['gender'] == 'female']
print((len(female_population.index) / len(population.index)) * 100)