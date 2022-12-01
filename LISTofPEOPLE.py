import sqlite3
from sqlite3 import Error



def create_connection(path):
    sqlite_connection = None
    try:
        sqlite_connection = sqlite3.connect(path)
        print("База данных создана и успешно подключена к SQLite")
    except Error as error:
        print(f"Ошибка '{error}' при подключении к sqlite")
    return sqlite_connection
connection = create_connection("list.db")

def execute_query(connection, query):  # Создать таблицу
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

#
#
# try:
#     sqlite_create_table_LIST = '''CREATE TABLE LIST(
#          id INTEGER PRIMARY KEY,
#          surname surname TEXT NOT NULL,
#          name surname TEXT NOT NULL,
#          telephon INTEGER NOT NULL,
#          email INTEGER NOT NULL        );'''
#     execute_query(connection, sqlite_create_table_LIST)
#
# except sqlite3.Error as error:
#     print("Ошибка при подключении к sqlite", error)
# finally:
#     if (connection):
#         connection.close()
#         print("Соединение с SQLite закрыто")


def insert_multiple_records(connection, records, sqlite_insert_query):  # Добавить элементы в таблицы
    cursor = connection.cursor()
    cursor.executemany(sqlite_insert_query, records)
    connection.commit()
    print("Записи успешно вставлены в таблицу LIST", cursor.rowcount)
    connection.commit()
    cursor.close()



try:
     sqlite_insert_query = """INSERT INTO LIST
                                 (id, surname, name, telephon, email )
                                 VALUES (?, ?, ?, ?, ?);"""
     records_to_insert = [(1, 'Revnev ', 'Alex', '4508811', '125@bk.ru'),
                            (2, 'Ivanov ', 'Oleg', '5895995', '325@bk.ru'),
                            (3, 'Smirnov ', 'Ivan', '325457', '215@bk.ru'),
                            (4, 'Egorov', 'Anton', '155545', '37373bk.ru'),
                          (5, 'Petrov', 'Anton','1435465', '5454@bk.ru'),
                          (6, 'Sergeev', 'Sergey','6545464', '45545@bk.ru'),
                          (7, 'Ragin', 'Evgenii',' 6574635', '554544@bk.ru'),
                          (8, 'Vasiliev ', 'Andrey', '2645484', '455@bk.ru')]

     insert_multiple_records(connection,records_to_insert, sqlite_insert_query)

except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
finally:
        if connection:
            connection.close()
            print("Соединение с SQLite закрыто")



def update_sqlite_table(connection, sql_update_query):  # Обновление/редактирование одной записи в таблице
    try:
        cursor = connection.cursor()
        cursor.execute(sql_update_query)
        connection.commit()
        print("Запись успешно обновлена")
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if connection:
            connection.close()
            print("Соединение с SQLite закрыто")


# update_query = """Update LIST set telephone = 1 where id = 3"""  # как сделать запрос и  ввести это с клаиватуры (как input())?
# update_sqlite_table(update_query)
#

def delete_sqlite_record(connection, dev_id):  # удаление записей
    try:
        cursor = connection.cursor()
        sql_update_query = """DELETE from LIST where id = ?"""
        cursor.execute(sql_update_query, (dev_id,))
        connection.commit()
        print("Запись успешно удалена")
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if connection:
            connection.close()
            print("Соединение с SQLite закрыто")


# id = int(input('введите номер Id, котрый нужно удлалить из таблицы'))
# delete_sqlite_record(id)


def read_sqlite_table(connection):
    try:
        connection = sqlite3.connect('list.db')
        cursor = connection.cursor()
        print("Подключен к SQLite")

        sqlite_select_query = """SELECT * from LIST"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        print("Всего строк:  ", len(records))
        print("Вывод каждой строки")
        for row in records:
            print("ID:", row[0])
            print("Фамилия:", row[1])
            print("Имя", row[2])
            print("Телефон:", row[3])
            print("эл. почта:", row[4])

        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if connection:
            connection.close()
            print("Соединение с SQLite закрыто")


# print(read_sqlite_table())


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")

# select = "SELECT * from LIST"
# users = execute_read_query(sqlite_connection, select)

# for student in users:
#      print(student)