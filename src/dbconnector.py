'''
Created By: <Cole Aydelotte>
'''
import mysql.connector

import os

from gui import Gui


def connect_to_my_SQL():
    cnx = mysql.connector.connect(password = 'project', user='project')
    cursor = cnx.cursor(buffered=True)
    return cursor, cnx


'''
    :param cursor: instance of the connection to the database
    :param DB_NAME: name of the database to create
    Creates the database at cursor with the given name.
    '''
def create_database(cursor, DB_NAME):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)


# CREATE TABLE `items` (
#   `item_id` int NOT NULL,S
#   `item_name` varchar(100) DEFAULT NULL,
#   `item_price` decimal(10,2) DEFAULT NULL,
#   `item_quantity` int DEFAULT NULL,
#   PRIMARY KEY (`item_id`)
# );
def make_items(cursor):
    sql = "CREATE TABLE `items` ( `item_id` int NOT NULL, `item_name` varchar(100) DEFAULT NULL, `item_price` decimal(10,2) DEFAULT NULL, `item_quantity` int DEFAULT NULL, PRIMARY KEY (`item_id`));"
    cursor.execute(sql)
    print("items table created")

# CREATE TABLE `transactions` (
#   `transaction_id` int NOT NULL AUTO_INCREMENT,
#   `total_price` decimal(10,2) DEFAULT NULL,
#   PRIMARY KEY (`transaction_id`))
def make_transactions(cursor):
    sql = "CREATE TABLE `transactions` ( `transaction_id` int NOT NULL AUTO_INCREMENT, `total_price` decimal(10,2) DEFAULT NULL, PRIMARY KEY (`transaction_id`));"
    cursor.execute(sql)
    print("transactions table created")
    
# CREATE TABLE `user_info` (
#   `transaction_id` int DEFAULT NULL,
#   `item_id` int DEFAULT NULL,
#   `item_amount` int DEFAULT NULL,
#   KEY `transaction_id` (`transaction_id`),
#   KEY `item_id` (`item_id`),
#   CONSTRAINT `user_info_ibfk_1` FOREIGN KEY (`transaction_id`) REFERENCES `transactions` (`transaction_id`),
#   CONSTRAINT `user_info_ibfk_2` FOREIGN KEY (`item_id`) REFERENCES `items` (`item_id`)
# )
def make_user_info(cursor):
    sql = "CREATE TABLE `user_info` (`transaction_id` int DEFAULT NULL, `item_id` int DEFAULT NULL, `item_amount` int DEFAULT NULL, KEY `transaction_id` (`transaction_id`), KEY `item_id` (`item_id`), CONSTRAINT `user_info_ibfk_1` FOREIGN KEY (`transaction_id`) REFERENCES `transactions` (`transaction_id`), CONSTRAINT `user_info_ibfk_2` FOREIGN KEY (`item_id`) REFERENCES `items` (`item_id`));"
    cursor.execute(sql)
    print("user_info table created")

def insert_data(cursor):
    infile = open("src/zitems.txt", "r")
    lines = infile.readlines()
    x = 0
    for line in lines:
        x += 1
        name, price, stock = line.split(",")

        query = f"INSERT INTO items (item_id, item_name, item_price, item_quantity) VALUES (%s, %s, %s, %s)"
        val = (x, name, price, stock)
        cursor.execute(query, val)
        cursor.execute("commit;")
    infile.close()
    print("item data inserted into Items table")

def check_data(cursor):
    data = open("src/zitems.txt", 'r')
    for line in data:
        lst = line.split(" ")
        name = lst[0]
        cursor.execute(f"SELECT item_quantity FROM items WHERE item_name = '{name}'")
        rows = cursor.fetchall()
        if rows:
            for row in rows:
                quantity = row[0]
                if int(quantity) == 0:
                    cursor.execute(f"DELETE FROM items WHERE item_name = '{name}'")

def main():
    made_db = False
    with open("src/holder.txt", 'r') as file:
        try:
            for line in file:
                print(line.strip())
                if line.strip() == "T":
                    made_db = True
                elif line.strip() == "F":
                    made_db = False
                break

        except Exception as e:
            print(f"An error occurred: {e}")

        finally:
            file.close()
    
    DB_NAME = 'DB_Final'
    cursor, connection = connect_to_my_SQL()
    with open("src/holder.txt", 'w') as file:
        if not made_db:
            cursor.execute("drop database if exists " + DB_NAME)
            create_database(cursor, DB_NAME)
            cursor.execute("USE {}".format(DB_NAME))
            make_items(cursor)
            make_transactions(cursor)
            make_user_info(cursor)
            insert_data(cursor)
            file.write("abcdefghijklmnopqrstuvwxyz")
    cursor.execute("USE {}".format(DB_NAME))
    check_data(cursor)
    with open("src/queries.txt", "r") as query_file:
        with open("src/solutions.txt", "w") as solution_file:
            for row in query_file:
                cursor.execute(row)
                solution_file.write(row)
                for line in cursor.fetchall():
                    solution_file.write(f"      {line}\n")
                solution_file.write(f"___________________________\n")
    print("Queries Executed")
    app = Gui(cursor)
    app.mainloop()
    connection.commit()
    cursor.close()
    connection.close()


main()
