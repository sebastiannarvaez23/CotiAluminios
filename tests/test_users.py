import pytest

@pytest.fixture
def user_creation():
    from django.contrib.auth.models import User
    return User(
        username = 'testusername',
        email = 'test@test.com',
        password = 'TestPass12345'
    )

@pytest.mark.django_db
def test_user_creation(user_creation):
    user_creation.save()
    assert user_creation.username == 'testusername'

@pytest.mark.django_db
def test_superuser_creation(user_creation):
    user_creation.is_superuser = True
    user_creation.is_staff = True
    user_creation.save()
    assert user_creation.is_superuser

@pytest.mark.django_db
def test_staff_user_creation(user_creation):
    user_creation.is_staff = True
    user_creation.save()
    assert user_creation.is_staff