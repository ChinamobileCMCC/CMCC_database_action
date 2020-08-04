import pymysql

db = pymysql.connect(host='', port=3306, user='', passwd='', db='testdb', charset='utf8')

cursor = db.cursor()

cursor.execute("select version()")

data = cursor.fetchone()

print(" Database Version:%s" % data)

cursor.execute("drop database if exists test")

sql = "create database test"

cursor.execute(sql)

cursor.execute("drop table if exists employee") 

sql = """

CREATE TABLE EMPLOYEE (

FIRST_NAME CHAR(20) NOT NULL,

LAST_NAME CHAR(20),

AGE INT,

SEX CHAR(1),

INCOME FLOAT )

"""

cursor.execute(sql)

sql = "select * from employee"

cursor.execute(sql)

data = cursor.fetchone()

print(data)

sql = "insert into employee values ('李','梅',20,'W',5000)"

cursor.execute(sql)

db.commit()


sql = "select * from employee"

cursor.execute(sql)

data = cursor.fetchone()

print(data)

sql = " select * from employee where income > '%d' " % (1000)

cursor.execute(sql)

data = cursor.fetchone()

print(data)

sql = " update employee set age = age+1 where sex = '%c' " % ('W')

cursor.execute(sql)

db.commit()


sql = "select * from employee"

cursor.execute(sql)

data = cursor.fetchone()

print(data)

sql = " delete from employee where age > '%d' " % (30)

cursor.execute(sql)

db.commit()

#查看更新后的结果

sql = "select * from employee"

cursor.execute(sql)

data = cursor.fetchone()

print(data)

db.close()
