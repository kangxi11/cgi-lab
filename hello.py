#!/usr/bin/env python3

import os
import cgi
import cgitb
import secret
from http.cookies import SimpleCookie
from templates import login_page, secret_page, after_login_incorrect

cgitb.enable()

form = cgi.FieldStorage()
username = form.getfirst('username')
password = form.getfirst('password')

print("Content-Type: text/html")
print()

if username == secret.username and password == secret.password:
    print('Set-Cookie: username=', username)
    print('Set-Cookie: password-', password)

cookies = SimpleCookie(os.environ['HTTP_COOKIE'])
cookie_username = None
cookie_password = None

if cookies.get('username'): cookie_username = cookies.get('username').value
if cookies.get('password'): cookie_password = cookies.get('password').value
if cookie_username == secret.username and cookie_password == secret.password:
    username = cookie_username
    password = cookie_password
print()

if not username and not password:
    print(login_page())
elif username == secret.username and password == secret.password:
    print(secret_page(username, password))
else:
    print(after_login_incorrect())

# print(os.environ['QUERY_STRING'])
# print(os.environ['HTTP_USER_AGENT'])
# print(os.environ)