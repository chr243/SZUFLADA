# -*- coding: utf-8 -*-

import sqlite3

def makedb():
    try:
        conn = sqlite3.connect('szuflada.db')
        c = conn.cursor()

        c.execute('''CREATE TABLE szuflada
                    (ID INTEGER PRIMARY KEY,
                    WIERSZ text,
                    PUNKTY text,
                    ZGLOSZONE text,
                    HASLO text)''')

        conn.commit()
        conn.close()
    except:
        print('tablica juz jest')

def addtodb(tekst, haslo):
    conn = sqlite3.connect('szuflada.db')
    c = conn.cursor()
    c.execute('INSERT INTO szuflada (HASLO, WIERSZ) VALUES (?, ?)', (haslo, tekst,))
    conn.commit()
    conn.close()

def showdb():
    conn = sqlite3.connect('szuflada.db')
    c = conn.cursor()
    c.execute("SELECT id, wiersz FROM szuflada")
    result = c.fetchall()
    conn.close()
    return result[::-1]

def dbfind(wpis):
    conn = sqlite3.connect('szuflada.db')
    c = conn.cursor()
    c.execute('SELECT id, wiersz FROM szuflada WHERE id = ?', (wpis,))
    result = c.fetchone()
    conn.close()
    return result[1]

def dbcheckpass(wpis):
    conn = sqlite3.connect('szuflada.db')
    c = conn.cursor()
    c.execute('SELECT haslo FROM szuflada WHERE id = ?', (wpis,))
    result = c.fetchone()
    conn.close()
    return result

def dbremove(wpis):
    conn = sqlite3.connect('szuflada.db')
    c = conn.cursor()
    c.execute('DELETE FROM szuflada WHERE id = ?', (wpis,))
    conn.commit()
    conn.close()
    return 'ok'


