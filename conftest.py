import pytest
from fixture.application import Application


@pytest.fixture(scope="session")  # фикстура создается одна на всю сессию
def app(request):
    fixture = Application()  # Инициализация фикстуры
    fixture.session.login(username="admin", password="secret")
    request.addfinalizer(fixture.destroy)  # Как должна быть разрушена фикстура
    return fixture
