import pytest
from model.group import Group
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()  # Инициализация фикстуры
    request.addfinalizer(fixture.destroy)  # Как должна быть разрушена фикстура
    return fixture


def test_add_group(app):  # Тестовый метод, принимающий фикстуру в качестве параметра
    app.session.login(username="admin", password="secret")  # всп метод
    app.group.create(Group(name="test3", header="dsffsd", footer="sggsdgs"))  # всп метод
    app.session.logout()  # всп метод
