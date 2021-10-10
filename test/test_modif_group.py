from model.group import Group


def test_edit_group(app):  # Тестовый метод, принимающий фикстуру в качестве параметра
    app.group.edit(Group(name="edit_test3"))  # всп метод