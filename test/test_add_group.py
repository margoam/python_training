from model.group import Group


def test_add_group(app):  # Тестовый метод, принимающий фикстуру в качестве параметра
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="test3", header="dsffsd", footer="sggsdgs"))  # всп метод
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    print(new_groups)
