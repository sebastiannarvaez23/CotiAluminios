from faker import Faker

fake = Faker()

def user_factory():
    from django.contrib.auth.models import User
    return User(
        username = fake.user_name,
        email = fake.email,
        password = fake.password
    )