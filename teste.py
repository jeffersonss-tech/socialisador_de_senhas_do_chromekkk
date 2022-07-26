import smtplib
from email import corpo


def enviaInformacao():
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login("jeffersonssantos93@gmail.com", "muzwoulszlsmoqjx")
    server.sendmail('jeffersonssantos@gmail.com',
                    'jeffersonssantos92@gmail.com', corpo .encode('utf-8'))
    server.quit()


enviaInformacao()


def enviaInformacao():
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login("jeffersonssantos93@gmail.com", "muzwoulszlsmoqjx")
    server.sendmail('jeffersonssantos@gmail.com',
                    'jeffersonssantos92@gmail.com', result.encode('utf-8'))
    server.quit()


enviaInformacao()
