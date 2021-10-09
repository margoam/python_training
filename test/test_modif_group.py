from model.group import Group


def test_edit_group(app):  # Тестовый метод, принимающий фикстуру в качестве параметра
    app.session.login(username="admin", password="secret")  # всп метод
    app.group.edit(Group(name="edit_test3"))  # всп метод
    app.session.logout()  # всп метод