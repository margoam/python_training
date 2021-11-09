import pymysql  # данный пакет используется для работы с БД
from fixture.orm import ORMFixture


# соединение с БД
db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    l = db.get_contact_list()
    for items in l:
        print(items)
    print(len(l))
finally:
    pass  # db.destroy()
