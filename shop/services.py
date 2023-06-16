from django.conf import settings
from django.core.mail import get_connection, EmailMessage


def send_mail_to_address(name: str, phone: str, email: str):
        with get_connection(
                host=settings.EMAIL_HOST,
                port=settings.EMAIL_PORT,
                username=settings.EMAIL_HOST_USER,
                password=settings.EMAIL_HOST_PASSWORD,
                use_tls=settings.EMAIL_USE_TLS
        ) as connection:
            subject = "Новый заказ"
            email_from = settings.EMAIL_HOST_USER
            recipient_list = ["ЗДЕСЬ емейл челов которым отправлять", ]
            message = "Тут хороший шаблон для сообщения"
            EmailMessage(subject, message, email_from, recipient_list, connection=connection).send()