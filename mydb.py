import mysql.connector

dataBase= mysql.connector.connect(
    host="localhost",
    user="root",
    passwd='qwerty'
)

cursorObject=dataBase.cursor()

cursorObject.execute("CREATE DATABASE mydb")

print("All done!")
