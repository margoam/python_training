import pymysql  # данный пакет используется для работы с БД
from model.group import Group
from model.contact import Contact


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        # autocommit=True - сбрасывание кеша после каждого запроса
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

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

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()  # указатель на данные в БД
        try:
            cursor.execute("select id, firstname, middlename, lastname, nickname, address, home, mobile, work, fax, "
                           "email, email2, email3, bday, bmonth, byear, notes, phone2, deprecated from addressbook where deprecated='0000-00-00 00:00:00'")  # выполнение запроса
            for row in cursor:
                (id, first_name, middle_name, last_name, nick_name, address, home_number, mobile_number, work_number, fax_number, email, email2, email3,
                 birth_day, birth_month, birth_year, notes, second_number) = row
                list.append(Contact(id=str(id), first_name=first_name, middle_name=middle_name, last_name=last_name,
                                    nick_name=nick_name, address=address, home_number=home_number, mobile_number=mobile_number,
                                    work_number=work_number, fax_number=fax_number, email=email, email2=email2, email3=email3,
                                    birth_day=birth_day, birth_month=birth_month, birth_year=birth_year, notes=notes, second_number=second_number))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()
