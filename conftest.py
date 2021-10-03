import pytest
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()  # Инициализация фикстуры
    request.addfinalizer(fixture.destroy)  # Как должна быть разрушена фикстура
    return fixture
