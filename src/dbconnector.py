'''
Created By: <Cole Aydelotte>
'''
import mysql.connector

def connectToMySQL():
    cnx = mysql.connector.connect(password = 'project', user='project')
    cursor = cnx.cursor()
    return cursor, cnx

'''
    :param cursor: instance of the connection to the database
    :param DB_NAME: name of the database to create
    Creates the database at cursor with the given name.
    '''
def createDatabase(cursor, DB_NAME):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

# CREATE TABLE items (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     name VARCHAR(100),
#     price DECIMAL(10, 2),
#     stock INT
# );

def makeTable(cursor):
    sql = "CREATE TABLE items (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100), price DECIMAL(10, 2), stock INT);"
    cursor.execute(sql)
    print("items table created")

def insertData(cursor):
    infile = open("zitems.txt", "r")
    header = infile.readline()
    record = ''
    data = ''

    for line in infile:
        sql = ""
        line = line.strip()
        record = line.split(",")
        data = ""

        for i in range(3):
            if record[i] == "NULL":
                data += "NULL,"
            else:
                data += "'" + record[i] + "', "

        data = data[:-2]
        sql = "INSERT INTO items VALUES (" + data + ");"
        cursor.execute(sql)
    infile.close()
    print("item data inserted into Items table")

def main():
    DB_NAME = 'DB_Final'
    cursor, connection = connectToMySQL()
    cursor.execute("drop database if exists " + DB_NAME)
    createDatabase(cursor, DB_NAME)
    cursor.execute("USE {}".format(DB_NAME))
    makeTable(cursor)
    insertData(cursor)
    put = print(input("what would you like to search?"))
    cursor.execute("select * from items like %" + put + "%;")
    connection.commit()
    cursor.close()
    connection.close()

main()