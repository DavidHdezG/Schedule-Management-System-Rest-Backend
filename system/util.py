from django.core.mail import EmailMessage
import threading


class EmailThread(threading.Thread):
    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()


class Util:
    @staticmethod
    def send_email(id, password):
        email = EmailMessage(
            subject='Thank you for registering to our site',
            body=' Your password is: ' + password,
            to=[str(id) + '@uach.mx',]
        )
        EmailThread(email).start()
