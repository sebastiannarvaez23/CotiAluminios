import factory

from django.contrib.auth.models import User
from faker import Faker

fake = Faker()

class UserCommonFactory(factory.django.DjangoModelFactory):
    
    class Meta:
        model = User

    username = fake.user_name()
    email = fake.email()
    is_staff = False
    is_superuser = False

class UserStaffFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = User

    username = fake.user_name()
    email = fake.email()
    is_staff = True
    is_superuser = False

class UserSuperuserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = User

    username = fake.user_name()
    email = fake.email()
    is_staff = True
    is_superuser = True