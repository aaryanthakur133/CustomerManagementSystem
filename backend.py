import os
import mysql.connector
import datetime
mydb= mysql.connector.connect(host="localhost",user="root",password=os.getenv("DB_PASSWORD", ""),database="CustomerManagement")
# to insert data from database

u_id=input("Enter user id :")

namee= input("Enter user name :")

pws=input("enter user password :")

c= mydb.cursor()

c.execute("insert into Users values(%s,%s,%s)",(u_id,namee,pws))
mydb.commit()
print("User enter successfully")
