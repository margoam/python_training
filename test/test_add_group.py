from model.group import Group


def test_add_group(app):  # Тестовый метод, принимающий фикстуру в качестве параметра
    old_groups = app.group.get_group_list()
    group = Group(name="test3", header="dsffsd", footer="sggsdgs")
    app.group.create(group)  # всп метод
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
