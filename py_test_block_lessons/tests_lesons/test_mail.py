import pytest

@pytest.fixture()
def set_up():
    print('user is logged in')
    yield # выполниться после завершения текущего теста
    print(' user has logged out')

def test_send_mail(set_up):
    print('mail was send')

def test_send_mail_1(set_up):
    print('mail was send')


