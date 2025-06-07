#1.    Завантажте CSV-файл (див. тут).
#2.    Виведіть перші 5 і останні 5 рядків, щоб оглянути структуру даних.
#3.    Видаліть усі рядки з пропущеними значеннями, а також усі дублі.
#4.    Замініть пропущені значення у стовпці з ціною на середнє значення цього стовпця.

import pandas as pd

#1

df=pd.read_csv('extended_sales_data.csv')

#2

print(df.head())
print(df.tail())
print(df.describe())

#3

df2=df.copy()

print(df2.head())
print(df2.tail())

df.dropna(inplace=True)
df.drop_duplicates(inplace=True)


print(df.head())
print(df.tail())
print(df.describe())

#4

mean_purchase=df2['Purchase_Amount'].mean()
print(mean_purchase)
df2['Purchase_Amount'].fillna(mean_purchase,inplace=True)
print(df2.head())
