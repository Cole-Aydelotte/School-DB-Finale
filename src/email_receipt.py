import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(user_email, list_of_Items, cursor):
    sender_email = 'database.systems.final@gmail.com'
    receiver_email = user_email
    password = 'ccfivfapjvhkifcp'

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = 'Recent Purchase'

    body = ''
    total_price = 0
    items = list_of_Items
    for i in items:
        for x in items:
            cursor.execute(f"SELECT item_price FROM items WHERE item_name = '{x[0]}'")
            price = cursor.fetchone()[0]
            total_price += float(price)
        cursor.execute(f"INSERT INTO transactions (total_price) VALUES ({total_price})")
        cursor.execute("commit;")
        cursor.execute(f"SELECT LAST_INSERT_ID()")
        trans_id = cursor.fetchone()[0]
        if body == '':
            body += f"Transaction ID: {trans_id}, Total Price: {round(total_price, 2)}, {i[0]}"
        else:
            body += ', ' + i[0]

    message.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        print('Email sent successfully!')
    except Exception as e:
        print(f"Email could not be sent. Error: {str(e)}")
    finally:
        server.quit()