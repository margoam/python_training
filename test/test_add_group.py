from model.group import Group


def test_add_group(app, db, json_groups, check_ui):  # Тестовый метод, принимающий фикстуру в качестве параметра
    group = json_groups
    old_groups = db.get_group_list()
    app.group.create(group)  # всп метод
    new_groups = db.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
