import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from settings import DATABASE

# 初始化数据库连接，使用pymysql模块
engine = create_engine(URL(**DATABASE))
sql1 = '''SELECT t1.district_name as province,t2.district_name as city,t3.district_name as county FROM yxg_aux_address t1 LEFT JOIN yxg_aux_address t2 ON t1.row_id = t2.par_row_id LEFT JOIN yxg_aux_address t3 ON t2.row_id = t3.par_row_id LEFT JOIN yxg_aux_address t4 ON t3.row_id = t4.par_row_id WHERE t4.row_id is not null'''
df = pd.read_sql_query(sql1, engine)
df.drop_duplicates(subset=['city', 'county'], inplace=True)
# df['tmp'] = df['city'] + '|' + df['county']
df.insert(0, 'country', '中国')
df['lat'] = '0.0'
df['lng'] = '0.0'
df.rename(columns={'province': 'sheng', 'city': 'shi', 'county': 'qu'}, inplace=True)
df.to_csv("addressparser/pca.csv", sep=',', encoding='utf-8', index=False)
print(df)
