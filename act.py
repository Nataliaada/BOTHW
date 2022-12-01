import sqlite3


import LISTofPEOPLE as ST



connection = ST.create_connection("list.db")


def option():
    print("\nВас приветствует справочник!")
    ch = int(input('Введите , что хотите сделать: \n \
    1: Поиск ID  по имени \n \
    2: Посмотреть телефон \n \
    3: Добавить \n \
    4: Удалить \n \
    5: Редактировать запись \n \
    6: Вывести весь список  \n \
    7: Выход\n \
    Ваш выбор: '))

    if ch == 1:
        st = str(input("Введите имя : "))
        select_by_name = "SELECT name, id FROM LIST Where name LIKE \"" + st + "\""
        print(ST.execute_read_query(connection, select_by_name))
        exit()
    elif ch == 2:
        st = str(input("Введите номер телефона: "))
        select_by_name = "SELECT name, telephon FROM LIST Where telephon LIKE \"" + st + "\""
        print(ST.execute_read_query(connection, select_by_name))
        exit()
    elif ch == 3:
        sqlite_insert_query = """INSERT INTO LIST
# #                                  (id, surname, name, telephon,email )
# #                                  VALUES (?, ?, ?, ?,?);;"""
        records = input("Введите как в примере:(9, 'Иванов', 'Олег', '125457', '1222@bk.ru')")
        print(ST.insert_multiple_records(connection, records, sqlite_insert_query))
    elif ch == 4:
        st = input('Введите id , которого нужно удалить из базы')
        dev_id = " DELETE from LIST where id  LIKE \"" + st + "\""
        print(ST.delete_sqlite_record(connection, dev_id))

    elif ch == 5:
        st = input('Введите телефон который нужно исправить ')
        new =input('Введите телефон на  который нужно исправить ')
        update_query = "UPDATE   LIST   SET  telephon = \"" + new + "\"   WHERE   telephon = \"" + st + "\""
        ST.update_sqlite_table(connection, update_query)
    elif ch == 6:

        select = "SELECT * from LIST"
        users = ST.execute_read_query(connection, select)
        for student in users:
            print(student)
    else:
        print('еще раз')
    exit()

# option()
