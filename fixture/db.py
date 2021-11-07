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
                           "email, email2, email3, bday, bmonth, byear, notes, phone2 from addressbook")  # выполнение запроса
            for row in cursor:
                (id, firstname, middlename, lastname, nickname, address, home, mobile, work, fax, email, email2, email3,
                 bday, bmonth, byear, notes, phone2) = row
                list.append(Contact(id=str(id), first_name=firstname, middle_name=middlename, last_name=lastname,
                                    nick_name=nickname, address=address, home_number=home, mobile_number=mobile,
                                    work_number=work, fax_number=fax, email=email, email2=email2, email3=email3,
                                    birth_day=bday, birth_month=bmonth, birth_year=byear, notes=notes, second_number=phone2))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()
