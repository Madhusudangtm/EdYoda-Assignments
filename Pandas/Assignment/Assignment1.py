# importing libraries
import pandas as pd
url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user'
df = pd.read_csv(url, index_col = 'user_id', sep = '|')
df.head()

# See the first 10 and last 10 entries
print('------------first 10 entries------------\n',df.head(10),'\n------------last 10 entries------------\n',df.tail(10))

# What is the number of observations in the dataset?
obs = df.shape[0]
print('Number of Observations :', obs)

# What is the number of columns in the dataset?
ncol = df.shape[1]
print('Number of columns :', ncol)

# Print the name of all the columns.
print(df.columns)

# How is the dataset indexed?
indexed = df.index
print(indexed)

# What is the data type of each column?
print(df.dtypes)

# Print only the occupation column
print(df['occupation'])

# How many different occupations are in this dataset?
print(df['occupation'].nunique())

# How many different occupations are in this dataset?
print(df['occupation'].value_counts().count())

# What is the most frequent occupation?
print(df['occupation'].mode())

# What is the most frequent occupation?
print(df['occupation'].value_counts().sort_values(ascending=False).head())

# DataFrame Info.
print(df.info())

# Describe all the columns
print(df.describe(include='all'))

# Summarize only the occupation column
print(df['occupation'].describe())

# What is the mean age of users?
print(df['age'].mean())

# What is the age with least occurrence?
print(df['age'].min())