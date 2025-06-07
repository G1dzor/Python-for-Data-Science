import pandas as pd
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
