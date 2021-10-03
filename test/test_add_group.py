from model.group import Group


def test_add_group(app):  # Тестовый метод, принимающий фикстуру в качестве параметра
    app.session.login(username="admin", password="secret")  # всп метод
    app.group.open_groups_page()
    app.group.create(Group(name="test3", header="dsffsd", footer="sggsdgs"))  # всп метод
    app.session.logout()  # всп метод
