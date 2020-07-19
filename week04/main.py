import pandas as pd
import numpy as np
import pymysql

# 测试数据 data/table1
table1 = data = pd.DataFrame({
    'id': [i for i in range(20)],
    'age': [i for i in np.random.randint(0, 100, 20)],
    'order_id': [i for i in np.random.randint(1, 10, 20)]
})

# print(f'测试数据 data/table1\n{data}\n')

# 测试数据 table2
table2 = pd.DataFrame({
    'id': [i for i in range(20)],
    'age': [i for i in np.random.randint(0, 100, 20)],
    'order_id': [i for i in np.random.randint(1, 10, 20)]
})

# print(f'测试数据 table2\n{table2}\n')

# 1. SELECT * FROM data;
print(' 1 '.center(79, '-'))

setting = pd.read_json('mysql_setting.json', typ='series').to_dict()

try:
    conn = pymysql.connect(
        host=setting['host'],
        user=setting['user'],
        password=setting['password'],
        db=setting['db'],
        charset=setting['charset'],
    )
except Exception:
    print('failed to connect to MySQL')
else:
    with conn:
        print(pd.read_sql('SELECT * FROM data', conn))

# 2. SELECT * FROM data LIMIT 10;
print(' 2 '.center(79, '-'))

print(data.head(10))

# 3. SELECT id FROM data;  //id 是 data 表的特定一列
print(' 3 '.center(79, '-'))

print(data['id'])

# 4. SELECT COUNT(id) FROM data;
print(' 4 '.center(79, '-'))

print(data['id'].count())

# 5. SELECT * FROM data WHERE id<1000 AND age>30;
print(' 5 '.center(79, '-'))

print(data[(data['id'] < 1000) & (data['age'] > 30)])

# 6. SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;
print(' 6 '.center(50, '-'))

count_data = table1.drop_duplicates('order_id').groupby('id').agg(
    {'id': 'count'})
count_data.columns = ['sum']
print(count_data)

# 7. SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;
print(' 7 '.center(50, '-'))

print(pd.merge(table1, table2, on='id'))

# 8. SELECT * FROM table1 UNION SELECT * FROM table2;
print(' 8 '.center(79, '-'))

print(pd.merge(table1, table2, how='outer'))

# 9. DELETE FROM table1 WHERE id=10;
print(' 9 '.center(79, '-'))

print(table1[table1['id'] != 10])

# 10. ALTER TABLE table1 DROP COLUMN column_name;
print(' 10 '.center(79, '-'))

print(table1.drop(columns='id'))
