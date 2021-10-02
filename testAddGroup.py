import pytest
from group import Group
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()  # Инициализация фикстуры
    request.addfinalizer(fixture.destroy)  # Как должна быть разрушена фикстура
    return fixture


def test_add_group(app):  # Тестовый метод, принимающий фикстуру в качестве параметра
    app.login(username="admin", password="secret")  # всп метод
    app.create_group(Group(name="test3", header="dsffsd", footer="sggsdgs"))  # всп метод
    app.logout()  # всп метод
