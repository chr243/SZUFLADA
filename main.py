# -*- coding: utf-8 -*-

from bottle import run, route, post, request, get, template
from dbmanager import addtodb, showdb, dbfind, dbremove


@get('/add')
def addpls():
    return template('add.html')

@post('/added')
def added():
    wiersz = request.forms.wiersz
    haslo = request.forms.haslo
    addtodb(wiersz, haslo)
    return 'dodano: %s<br><br><br><a href="./">wroc</a>' % wiersz

@route('/')
def pokaz():
    db = showdb()
    return template('templejt.html', db=db)

@route('/pokaz/<numer>')
def pokaz(numer):
    wpis = dbfind(numer)
    return template('pokaz.html', numer=numer, wpis=wpis)

@route('/usun/<numer>')
def usun(numer):
    dbremove(numer)
    return 'usunieto %s<br><br><a href="../">wroc</a>' % numer 

run(host='0.0.0.0', port='80')
# DODAJ POLE HASLO DO DODAWARKI
# SPRAWDZANIE HASLO PODCZAS USUWANIA
# PANEL ADMINA
# OGARNIJ PUNKTY, CHOCIAZ TO MOZE NA KONCU

