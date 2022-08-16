from os import path

from redline import inicia

if path.exists('file') is False:
    with open('file', 'w') as file:
        file.write('48738203')
    inicia()
