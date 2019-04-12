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

sql = "INSERT INTO Products (code, name, description, tags, createdAt, updatedAt) VALUES (%s, %s, %s, %s, %s, %s)"
val_1 = ("ANGSFT", "Angel Soft", "Two-ply toilet paper", "soft,tp", time.strftime('%Y-%m-%d %H:%M:%S'), time.strftime('%Y-%m-%d %H:%M:%S'))
val_2 = ("DIXCP", "Dixie", "Paper Cups 20 pk.", "cups, paper", time.strftime('%Y-%m-%d %H:%M:%S'), time.strftime('%Y-%m-%d %H:%M:%S'))
val_3 = ("BRWNY", "Brawny", " Paper Towels Extra Strong", "paper, towels", time.strftime('%Y-%m-%d %H:%M:%S'), time.strftime('%Y-%m-%d %H:%M:%S'))
val_4 = ("MNPKNS", "Mardi Gras", "Napkins 50 pk.", "paper, napkins", time.strftime('%Y-%m-%d %H:%M:%S'), time.strftime('%Y-%m-%d %H:%M:%S'))
val_5 = ("VNPKNS", "Vanity Fair", "Napkins 20 pk.", "paper, napkins", time.strftime('%Y-%m-%d %H:%M:%S'), time.strftime('%Y-%m-%d %H:%M:%S'))
val_6 = ("DLLHS", "Doll House", "3 Bedroom Doll House", "doll, house", time.strftime('%Y-%m-%d %H:%M:%S'), time.strftime('%Y-%m-%d %H:%M:%S'))
val_7 = ("VTMNS", "Vitamins", "Adult Gummies", "gummies, vitamins", time.strftime('%Y-%m-%d %H:%M:%S'), time.strftime('%Y-%m-%d %H:%M:%S'))
val_8 = ("SDCRD", "SD Card", "128 GB", "sd, gb, card", time.strftime('%Y-%m-%d %H:%M:%S'), time.strftime('%Y-%m-%d %H:%M:%S'))
val_9 = ("CPTNCR", "Captain Crunch", "Peanut Butter", "peanut, butter, captian, crunch", time.strftime('%Y-%m-%d %H:%M:%S'), time.strftime('%Y-%m-%d %H:%M:%S'))
val_10 = ("GFTCRD", "Gift Card", "Applebee's", "gift, card, applebees", time.strftime('%Y-%m-%d %H:%M:%S'), time.strftime('%Y-%m-%d %H:%M:%S'))


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

mydb.commit()

print(mycursor.rowcount, "record inserted.")
