import mysql.connector

cnx = mysql.connector.connect(user='project', password='project',
                              host='localhost',
                              database='astronaut')
cnx.close()