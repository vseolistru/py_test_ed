import pytest


@pytest.fixture()
def set_up():
    print('user is logged in')
    yield # выполниться после завершения текущего теста
    print(' user has logged out')

@pytest.fixture(scope='function')
# scope = 'module' вызовет поочередно каждый тест после начала, выполнит и только потом выполнит передачу
# управления yield
# scope='function' вызовет и выполнит каждый тест последовательно и передаст управление yield
def some_func():
    print('start testing')
    yield # выполниться после завершения текущего теста
    print('finish')