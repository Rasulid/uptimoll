# import sys
# sys.path.append("...")
from factory.alchemy import SQLAlchemyModelFactory
from models import UserInfo
from faker import Faker

fake = Faker()
model = UserInfo()


class UserInfoFactory(SQLAlchemyModelFactory):
    """This class give the fake user info"""
    global model

    model.name = fake.name()

    name = fake.name()
    print(name)
