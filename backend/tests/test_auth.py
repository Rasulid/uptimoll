import requests
import pytest
from auth import authenticate_user, login_for_access_token

ENPOINT = "http://127.0.0.1:9090"


def calc():
    return 10


def test_calc():
    assert calc() == 10


def test_login():
    username = "root"
    password = "root"
    auth = login_(username, password)
    assert auth.status_code == 200


def login_(username, password):
    return requests.post(ENPOINT + "/auth/token")
