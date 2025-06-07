import pandas as pd
import numpy as np
from sqlalchemy import create_engine

user='user'
password='password'

host='localhost'
port=3306
database='my_database'

connection_url=f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}"

conn=create_engine(connection_url)

query="SELECT * FROM titanic"
df = pd.read_sql(query,con=conn)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', None)
print(df)
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
numeric_cols_for_conversion = ['Age', 'Fare', 'Pclass', 'SibSp', 'Parch', 'Survived']
for col in numeric_cols_for_conversion:
    df[col] = pd.to_numeric(df[col], errors='coerce')
#1
numeric_cols = ['Age', 'Fare', 'Pclass', 'SibSp', 'Parch', 'Survived']
new_df=df[numeric_cols].copy()
print(new_df.head(15))
#2
clean_df=new_df.dropna()
print(clean_df.head(15))
#3
correlation_matrix = clean_df.corr(method='spearman')

print("Кореляційна матриця (Спірмен):")
print(correlation_matrix)

#4
correlation_with_survived = correlation_matrix['Survived'].sort_values(ascending=False)
print("Змінні, відсортовані за кореляцією з 'Survived':")
print(correlation_with_survived)

