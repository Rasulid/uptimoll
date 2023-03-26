from factory.alchemy import SQLAlchemyModelFactory
from models import UserInfo
from faker import Faker

fake = Faker()
# model = UserInfo()


class UserInfoFactory(SQLAlchemyModelFactory):
    """This class give the fake user info"""
    class Meta:
        model = UserInfo

    name = fake.name()
    course = fake.job()
    phone_number = fake.phone_number()


