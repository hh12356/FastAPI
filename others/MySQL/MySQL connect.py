import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    port='3306',
    user='root',
    password='_password123'
)

cursor = connection.cursor()

cursor.execute("USE `Company`;")
# 也可以在连接处写要哪个资料库 database = 'xxx'
cursor.execute("SELECT * FROM `employee`;")
records = cursor.fetchall()
for r in records:
    print(r)

# cursor.execute("DELETE FROM `branch` WHERE `branch_id`=5;")
# connection.commit()
# 凡是修改数据都要commit

cursor.close()
connection.close()













