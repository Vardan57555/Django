

import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'ars19762002',
)


cursorObject = database.cursor()

cursorObject.execute('Create database elderco')

print('All Done')