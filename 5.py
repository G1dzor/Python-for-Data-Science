#1.    Завантажте дані, що містять інформацію про продажі в різних містах (див. тут)
#2.    Обчисліть середній дохід для кожного міста та виведіть результати у вигляді таблиці.
#3.    Знайдіть місто з найвищим і найнижчим доходом.
#4.    Відобразьте кількість транзакцій для кожного місяця, використовуючи групування за датою.

import pandas as pd

#1

df=pd.read_csv('transaction_analysis_data.csv')
print(df.head())
df.info()
df['Transaction_Date'] = pd.to_datetime(df['Transaction_Date'])
#2
income_by_city=df.groupby('City')['Transaction_Amount'].mean()
print(income_by_city)
#3
max_inc=income_by_city.idxmax()
min_inc=income_by_city.idxmin()
print(max_inc)
print(min_inc)
#4
df['Month'] = df['Transaction_Date'].dt.to_period('M')
by_month=df.groupby(['Month'])['Transaction_Amount'].sum()
by_month.sort_values()
print(by_month)