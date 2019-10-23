"""
mysql.py
"""
import pymysql

# 连接数据库
db = pymysql.connect(host='localhost', port=3306, user='root',
                     password='123456', database='stu', charset='utf8')
# 生成游标对象（操作数据库，执行sql语句）
cur = db.cursor()
# 执行各种对数据库的写操作
try:
    # 执行增删改操作
    # sql = "insert into class1 (name,age,score) values ('David',15,76);"
    # cur.execute(sql)

    # sql = "update class1 set sex='m' where name='David';"

    # sql = "delete from class1 where name='David';"

    # name = input("Name:")
    # age = int(input("Age:"))
    # score = float(input("Score:"))
    # sql = "insert into " \
    #       "class1 (name,age,score) values (%s,%s,%s);"
    # cur.execute(sql,[name,age,score])

    exe = []
    for i in range(3):
        name = input("Name:")
        age = int(input("Age:"))
        score = float(input("Score:"))
        exe.append((name, age, score))
    sql = "insert into " \
          "class1 (name,age,score) values (%s,%s,%s);"
    cur.executemany(sql, exe)
    db.commit()  # 将操作结果立即提交
except Exception as e:
    db.rollback()  # 事务回滚
    print(e)

# 关闭游标和数据库连接
cur.close()
db.close()
