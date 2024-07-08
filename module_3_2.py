def send_email(massage, recipient, *, sender="university.help@gmail.com"):
    def error_email(email):
        return '@' in email or email.endswith('.com') or email.endswith('.net') or email.endswith('.ru')
    if not error_email(sender) or not error_email(recipient):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif recipient == sender:#'urban.student@mail.ru':
        print('Нельзя отправить письмо самому себе!')
    elif sender == ('university.help@gmail.com'):
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!','urban.fan@mail.ru)',
           sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru',
           sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru',
           sender='urban.teacher@mail.ru')