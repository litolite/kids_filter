# -*- coding: utf-8 -*-
import sqlite3
conn = sqlite3.connect('my.db')
c = conn.cursor()

#Функция занесения пользователя в базу
def add_user(username,userpass):
    c.execute("INSERT INTO users (name,password) VALUES ('%s','%s')"%(username,userpass))
    conn.commit()

#Вводим данные
name = input("Введите Логин\n")
passwd = input("Введите Пароль\n")
print('\n')

#Делаем запрос в базу
print("Список пользователей:\n")
add_user(name,password,first_name,last_name)
c.execute('SELECT * FROM users')
row = c.fetchone()

#выводим список пользователей в цикле
while row is not None:
   print("id:"+str(row[0])+" Логин: "+row[1]+" | Пароль: "+row[2])
   row = c.fetchone()

# закрываем соединение с базой
c.close()
conn.close()