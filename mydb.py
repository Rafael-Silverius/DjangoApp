import mysql.connector

dataBase= mysql.connector.connect(
    host="localhost",
    user="root",
    passwd='qwerty'
)

cursorObject=dataBase.cursor()

cursorObject.execute("CREATE DATABASE mydb")

print("All done!")

 git config --global user.name "Rafael Walder"
$ git config --global user.email "rafaelwalder99@gmail.com"
$ git config --global push.default matching
$ git config --global alias.co checkout
$ git init