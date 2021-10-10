from model.group import Group


def test_edit_group(app):  # Тестовый метод, принимающий фикстуру в качестве параметра
    if app.group.count() == 0:
        app.group.create(Group(name="test4", header="header_test", footer="footer_test"))
    app.group.edit(Group(name="edit_test3"))  # всп метод