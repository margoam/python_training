from model.group import Group


def test_add_group(app):  # Тестовый метод, принимающий фикстуру в качестве параметра
    app.group.create(Group(name="test3", header="dsffsd", footer="sggsdgs"))  # всп метод
