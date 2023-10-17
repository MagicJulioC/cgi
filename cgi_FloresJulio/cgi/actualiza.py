#!C:/Users/jcfm_/AppData/Local/Programs/Python/Python311/python.exe
import mysql.connector
import os
import cgi
import cgitb
cgitb.enable()
print("Content-type: text/html")
print()
metodo = os.environ["REQUEST_METHOD"]

if metodo == "POST":
    datos = cgi.FieldStorage()
    e = datos.getvalue("email")
    p = datos.getvalue("password")
    n = datos.getvalue("name")
    a = datos.getvalue("avatar")
    r = datos.getvalue("role")

    con = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='foro')
    cur = con.cursor()
    sql = "UPDATE users SET password=sha1('{}'), name='{}', avatar='{}', role='{}' WHERE email='{}'".format(p, n, a, r, e)
    cur.execute(sql)
    con.commit()
    con.close()
    print("<h1>Usuario  Actualizado</h1>")
else:
    print("<h1>Metodo no Permitido</h1>")