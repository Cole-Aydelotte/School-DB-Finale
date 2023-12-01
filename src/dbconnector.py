'''
Created By: <Cole Aydelotte>
'''
import mysql.connector

def connectToMySQL():
    cnx = mysql.connector.connect(password = 'project', user='project')
    cursor = cnx.cursor(buffered=True)
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
    # zItems contains 3 values:
    # name, decimal price, integer

    infile = open("zitems.txt", "r")
    lines = infile.readlines()
    x = 0
    for line in lines:
        x += 1
        name, price, stock = line.split(",")


        query = f"INSERT INTO items (name, price, stock) VALUES (%s, %s, %s)"
        print(f"{x} inserted name {name}, price {price}, stock {stock}")
        val = (name, price, stock)
        cursor.execute(query, val)
        cursor.execute("commit;")
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
    put = input("what would you like to search?\n")
    query = f'SELECT name FROM items WHERE name LIKE "%{put}%";'
    pri = cursor.execute(query)
    print(pri)
    connection.commit()
    cursor.close()
    connection.close()

main()