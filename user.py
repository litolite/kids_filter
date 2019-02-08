import os
import binascii
import hashlib

from typing import Optional
from getpass import getpass

from prj_utils.db_session import session
from prj_utils.models import User


# Функция хэширования пароля перед созранением пароля

def hash_password(password: str) -> str:
    """
    Hash a password for storing.

    :param password:
    :return: hashed password

    """
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('utf-8')
    password_hash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),
                                        salt, 100000)
    password_hash = binascii.hexlify(password_hash)
    return (salt + password_hash).decode('utf-8')


# Функция проверки захешированного пароля

def verify_password(stored_password: str,
                    provided_password: str) -> bool:
    """
    Verify a stored password against one provided by user

    :param stored_password: user stored password
    :param provided_password: user provided password
    :return: boolean
    """
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    password_hash = hashlib.pbkdf2_hmac('sha512',
                                        provided_password.encode('utf-8'),
                                        salt.encode('utf-8'),
                                        100000)
    password_hash = binascii.hexlify(password_hash).decode('utf-8')
    return password_hash == stored_password


# Функция занесения пользователя в базу

def add_user(username: str,
             password: str,
             first_name: Optional[str] = None,
             is_admin: bool = True) -> bool:
    """
    Function for adding users into database

    :param username: user login
    :param userpass: user password
    :param first_name: user first name (if entered, else None)
    :param is_admin: True if he has admin functionality
    :return: True if user was created and False if not
    """
    sess = session()
    is_user_exists = sess.query(User).filter(
            User.username == username.strip().lower()
        ).count()

    print(is_user_exists)

    if is_user_exists > 0:
        sess.close()
        return False
    else:
        sess.add(
            User(username=username.strip().lower(),
                 password=hash_password(password),
                 first_name=first_name,
                 is_admin=is_admin
                 )
        )
        sess.commit()
        sess.close()

    return True


def get_users_from_database():
    sess = session()
    users = sess.query(User).all()
    sess.close()
    return users


def main(): # TODO не работает из IDE, не возвращает правильные ретурны из cmd (0, 1)
    username = input("Введите Логин: ")
    pswd = getpass("Введите Пароль: ")
    first_name = input("Введите ваше Имя (не обязательно): ")
    is_added = add_user(username, pswd, first_name)
    if is_added:
        return 'Пользователь добавлен в базу данных'
    else:
        return'Ошибка при добавлении пользователя.' \
              'Возможно такой пользователь уже существует.'


if __name__ == '__main__':
    main()
    """users = get_users_from_database()
    for user in users:
        print(f"id: {user.id} Логин: {user.username} | Хэш пароля: {user.password}")
    print("\n")
    print(main())"""
