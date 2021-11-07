import pymysql  # данный пакет используется для работы с БД
from model.group import Group


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()  # указатель на данные в БД
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")  # выполнение запроса
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()
