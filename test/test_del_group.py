from model.group import Group


def test_delete_first_group(app):  # Тестовый метод, принимающий фикстуру в качестве параметра
    if app.group.count() == 0:
        app.group.create(Group(name="test3", header="dsffsd", footer="sggsdgs"))
    app.group.delete_first_group()

