from fastapi import Depends, HTTPException, status, APIRouter
import models
from schemas import CreateUser
from typing import Optional
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from Database import engine, SessionLocal
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from datetime import timedelta, datetime
from jose import jwt, JWTError

SECRET_KEY = "f9b41574aaeecc730adb46fc77650cabaeb1dd43ef177d7b5092df98ea701914"
ALGORITHM = "HS256"

oauth2_bearer = OAuth2PasswordBearer(tokenUrl="/auth/token/")

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
    responses={404: {"description": "Authenticate Error"}},
)

models.Base.metadata.create_all(bind=engine)


def get_db():
    global db
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def password_hash(password):
    if password is None:
        raise "password is None"
    return bcrypt_context.hash(password)


def verify_password(plain_password, hashed_password):
    if plain_password is None or hashed_password is None:
        raise "failed verify password"
    return bcrypt_context.verify(plain_password, hashed_password)


def authenticate_user(user: str, password: str, db):
    user = db.query(models.User).filter(models.User.username == user).first()

    if not user:
        return "user is not"
    if not verify_password(password, user.password):
        return "verify password is None"
    return user


def create_access_token(
        username: str, user_id: int, express_delta: Optional[timedelta] = None
):
    encode = {"username": username, "id": user_id}
    if express_delta:
        expire = datetime.utcnow() + express_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=20)
    encode.update({"exp": expire})
    return jwt.encode(encode, SECRET_KEY, ALGORITHM)


def create_refresh_token(
        username: str,
        user_id: int,
        express_delta: Optional[timedelta] = None
):
    encode = {"username": username, "id": user_id}
    if express_delta:
        expire = datetime.utcnow() + express_delta
    else:
        expire = datetime.utcnow() + timedelta(days=10)
    encode.update({"exp": expire})
    return jwt.encode(encode, SECRET_KEY, ALGORITHM)


async def get_current_user(token: str = Depends(oauth2_bearer)):
    pyload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    username: str = pyload.get("username")

    user_id: int = pyload.get("id")

    if username is None or user_id is None:
        return get_user_exceptions()

    return {"sub": username, "user_id": user_id}


# @router.post("/create_admin")
# async def create_admin(user: CreateUser,
#                        db: Session = Depends(get_db),
#                        login: dict = Depends(get_current_user)):
#     res = []
#     user_model = models.User()
#     user_model.username = user.username
#     user_model.email = user.email
#
#     if user_model:
#         user_name = db.query(models.User).all()
#         for x in user_name:
#             if user_model.username == x.username or user_model.email == x.email:
#                 raise HTTPException(status_code=status.HTTP_409_CONFLICT,
#                                     detail={'msg': f"{user_model.username} user is already exists"})
#     print(user_model.username)
#     hash_password = password_hash(user.password)
#
#     user_model.password = hash_password
#     return_user_model = user_model
#
#     get_refresh_token = create_refresh_token(user_model.username, user_model.id)
#     get_access_token = create_access_token(user_model.username, user_model.id)
#
#     db.add(user_model)
#     db.commit()
#     res.append(return_user_model)
#     return CreateUser(
#         username=res[0].username,
#         email=res[0].email,
#         password=res[0].password
#     )


@router.post("/token")
async def login_for_access_token(
        form_data: OAuth2PasswordRequestForm = Depends(),
        db: Session = Depends(get_db)
):
    user = authenticate_user(form_data.username, form_data.password, db=db)

    if not user:
        raise token_exception()
    token_expires = timedelta(minutes=20)
    token = create_access_token(user.username, user.id, express_delta=token_expires)
    get_refresh_token = create_refresh_token(user.username, user.id)

    return {"access_token": token,
            "refresh_token": get_refresh_token}


# Exceptions


def get_user_exceptions():
    credential_exceptions = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return credential_exceptions


def token_exception():
    token_exception_response = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect username or password",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return token_exception_response
