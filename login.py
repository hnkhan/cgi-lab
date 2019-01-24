#!/usr/bin/env python3
import cgi
import cgitb
import os
import json
from templates import login_page, secret_page, after_login_incorrect
from secret import username, password

cgitb.enable()

print("Content-Type: text/html")
#print()
#print("<!doctype html>")
#print(login_page())

#printing out username and password
# form = cgi.FieldStorage()
# print("USERNAME:")
# print(form.getvalue("username"))
# print("PASSWORD:")
# print(form.getvalue("password"))

#logging in
# form = cgi.FieldStorage()
# p_user = form.getvalue("username")
# p_password = form.getvalue("password")

# if ((p_user == username) and (p_password == password)):
#     print(secret_page(p_user, p_password))
# else:
#     print(login_page())


#set cookies
form = cgi.FieldStorage()
p_user = form.getvalue("username")
p_password = form.getvalue("password")

c_username = ""
c_password = ""

try:
    cookie_string = os.environ.get("HTTP_COOKIE")
    #print(cookie_string)
    cookie_pairs = cookie_string.split(";")
    for pair in cookie_pairs:
        key, val = pair.split("=")
        if ("username" in key):
            c_username = val
        elif ("password" in key):
            c_password = val

except:
    pass

if (c_username and c_password):
    print("\n\n")
    print(secret_page(c_username, c_password))

elif (os.environ.get("REQUEST_METHOD", "GET") == "POST"):
    if ((p_user == username) and (p_password == password)):
        #set username cookie
        print("Set-Cookie: username={};".format(p_user))
        #set password cookie
        print("Set-Cookie: password={};".format(p_password))

        print(secret_page(p_user, p_password))
    else:
        print(after_login_incorrect)

else:
    print(login_page())
