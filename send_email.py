import smtplib

client = smtplib.SMTP('localhost')


class SmtpSenderLibrary():
    def __init__(self):
        self.sender = "default_sender@test.com"

    def smtp_send_mail(self, receiver, message, subject):
        try:
            body = "Subject: {}\n\n{}".format(subject, message)
            receiver_list = receiver.split(",")
            client.sendmail(self.sender, receiver_list, body)
            print("Email sent!")
        except smtplib.SMTPException as e:
            raise e
        except Exception as e:
            raise e


if "__main__" == __name__:
    subject = input("Subject?")
    message = input("Body?")
    receiver = input("Recipient?")
    smtp_obj = SmtpSenderLibrary()
    smtp_obj.smtp_send_mail(receiver, message, subject)
