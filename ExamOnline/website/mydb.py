import mysql.connector
database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'tuan462002',
)

cursorObject = database.cursor()

cursorObject.execute("CREATE DATABASE examonline")
print("all done")