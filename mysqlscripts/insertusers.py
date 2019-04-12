#pip install mysqlclient
import mysql.connector
import hashlib
import time

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  passwd="mysqlpassword",
  database='sampledb',
  auth_plugin='mysql_native_password'
)

mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)

sql = "INSERT INTO Users (name, login, email, password, role, createdAt, updatedAt) VALUES (%s, %s, %s, %s, %s, %s, %s)"
val_1 = ("Dave Cross", "davidc", "dave@amazon.com",  hashlib.md5(b'123456').hexdigest(), "vendor", time.strftime('%Y-%m-%d %H:%M:%S'), time.strftime('%Y-%m-%d %H:%M:%S'))
val_2 = ("Chelsea Hess", "ch256", "chels.hess@gmail.com", hashlib.md5(b'password').hexdigest(), "customer", time.strftime('%Y-%m-%d %H:%M:%S'), time.strftime('%Y-%m-%d %H:%M:%S'))
val_3 = ("Makenzie Ortiz", "maor123", "makncheese@gmail.com", hashlib.md5(b'qwerty').hexdigest(), "customer", time.strftime('%Y-%m-%d %H:%M:%S'), time.strftime('%Y-%m-%d %H:%M:%S'))
val_4 = ("Micah Andrade", "and1", "micah.andrade@melapower.com", hashlib.md5(b'asdfgh').hexdigest(), "vendor", time.strftime('%Y-%m-%d %H:%M:%S'), time.strftime('%Y-%m-%d %H:%M:%S'))
val_5 = ("Stephany Compton", "stephy", "stephy@calstate.edu", hashlib.md5(b'123!@#qweQWE').hexdigest(), "employee", time.strftime('%Y-%m-%d %H:%M:%S'), time.strftime('%Y-%m-%d %H:%M:%S'))
val_6 = ("Barrett Keith", "bar1994", "Barman@bar.com", hashlib.md5(b'pa$$word').hexdigest(), "vender", time.strftime('%Y-%m-%d %H:%M:%S'), time.strftime('%Y-%m-%d %H:%M:%S'))
val_7 = ("Valentina Daniel", "valentine", "val@gmail.com", hashlib.md5(b'betsyrocks').hexdigest(), "customer", time.strftime('%Y-%m-%d %H:%M:%S'), time.strftime('%Y-%m-%d %H:%M:%S'))
val_8 = ("Alvin Mccall", "chipmunk", "alvin.chipmunk@gmail.com", hashlib.md5(b'rockmysocks').hexdigest(), "customer", time.strftime('%Y-%m-%d %H:%M:%S'), time.strftime('%Y-%m-%d %H:%M:%S'))
val_9 = ("Baron Whitney", "whit1", "baron@gmail.com", hashlib.md5(b'sunshine').hexdigest(), "customer", time.strftime('%Y-%m-%d %H:%M:%S'), time.strftime('%Y-%m-%d %H:%M:%S'))
val_10 = ("Sincere Zhang", "zao", "szhang@company.com", hashlib.md5(b'tornado').hexdigest(), "employee", time.strftime('%Y-%m-%d %H:%M:%S'), time.strftime('%Y-%m-%d %H:%M:%S'))
val_11 = ("Jasmin Mcmahon", "jazz", "jazz@gmail.com", hashlib.md5(b'utah').hexdigest(), "customer", time.strftime('%Y-%m-%d %H:%M:%S'), time.strftime('%Y-%m-%d %H:%M:%S'))
val_12 = ("Essence Fowler", "flower", "flower@company.com", hashlib.md5(b'arizona').hexdigest(), "employee", time.strftime('%Y-%m-%d %H:%M:%S'), time.strftime('%Y-%m-%d %H:%M:%S'))
val_13 = ("Erin Hart", "heart", "erinh@amazon.com", hashlib.md5(b'californiagirl').hexdigest(), "vendor", time.strftime('%Y-%m-%d %H:%M:%S'), time.strftime('%Y-%m-%d %H:%M:%S'))
val_14 = ("Seth Floyd", "pink", "hey@gmail.com", hashlib.md5(b'heythatsme').hexdigest(), "customer", time.strftime('%Y-%m-%d %H:%M:%S'), time.strftime('%Y-%m-%d %H:%M:%S'))
val_15 = ("Jase Bender", "airbender", "bender@company.com", hashlib.md5(b'ilovebecca').hexdigest(), "admin", time.strftime('%Y-%m-%d %H:%M:%S'), time.strftime('%Y-%m-%d %H:%M:%S'))
val_16 = ("Christopher Thornton", "rosethorn", "Chris1234@gmail.com", hashlib.md5(b'CalState2012').hexdigest(), "customer", time.strftime('%Y-%m-%d %H:%M:%S'), time.strftime('%Y-%m-%d %H:%M:%S'))

print(val_16)
mycursor.execute(sql, val_1)
mycursor.execute(sql, val_2)
mycursor.execute(sql, val_3)
mycursor.execute(sql, val_4)
mycursor.execute(sql, val_5)
mycursor.execute(sql, val_6)
mycursor.execute(sql, val_7)
mycursor.execute(sql, val_8)
mycursor.execute(sql, val_9)
mycursor.execute(sql, val_10)
mycursor.execute(sql, val_11)
mycursor.execute(sql, val_12)
mycursor.execute(sql, val_13)
mycursor.execute(sql, val_14)
mycursor.execute(sql, val_15)
mycursor.execute(sql, val_16)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
