import pytest

@pytest.mark.django_db
def test_user_creation():
    from django.contrib.auth.models import User

    user = User.objects.create_user(
        username = 'testusername',
        email = 'test@test.com',
        password = 'TestPass12345'
    )

    assert user.username == 'testusername'

@pytest.mark.django_db
def test_superuser_creation():
    from django.contrib.auth.models import User

    user = User.objects.create_superuser(
        username = 'testusername',
        email = 'test@test.com',
        password = 'TestPass12345'
    )

    assert user.is_superuser

@pytest.mark.django_db
def test_staff_user_creation():
    from django.contrib.auth.models import User

    user = User.objects.create_user(
        username = 'testusername',
        email = 'test@test.com',
        password = 'TestPass12345',
        is_staff = True
    )

    assert user.is_staff