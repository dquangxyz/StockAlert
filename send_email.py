import smtplib


def send_email(from_email, password,to_email, message):
    try:
        server = "smtp.gmail.com"
        with smtplib.SMTP(server) as connection:
            connection.starttls()
            connection.login(user=from_email, password=password)
            connection.sendmail(from_addr=from_email, to_addrs=to_email, msg=message)
    except smtplib.SMTPAuthenticationError:
        server = "smtp.mail.yahoo.com"
        with smtplib.SMTP(server) as connection:
            connection.starttls()
            connection.login(user=from_email, password=password)
            connection.sendmail(from_addr=from_email, to_addrs=to_email, msg=message)




