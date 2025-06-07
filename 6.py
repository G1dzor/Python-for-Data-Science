#1.    Створіть два DataFrame: перший містить інформацію про клієнтів (ID, ім’я, вік), другий - інформацію про замовлення (ID клієнта, номер замовлення, сума). Файл 1 та Файл 2.
#2.    Виконайте злиття цих DataFrame за спільним полем ID клієнта.
#3.    Відфільтруйте дані, залишивши лише клієнтів віком більше 30 років, які здійснили замовлення на суму більше 100.
#4.    Обчисліть загальну суму замовлень для цих клієнтів.

import pandas as pd
#1
df_c=pd.read_csv('customer_data.csv')
df_o=pd.read_csv('order_data.csv')
#2
merged_df=pd.merge(df_c,df_o,on='Customer_ID')
print(merged_df.head())
#3
f_df=merged_df[(merged_df['Age']>30) & (merged_df['Order_Amount']>100)]
print(f_df.head())
#4
Sum=f_df['Order_Amount'].sum()
print(Sum)