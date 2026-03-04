from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_order_confirmation_email(order_id, customer_email):
    subject = f"Buyurtma #{order_id} tasdiqlandi"
    message = f"Assalomu alaykum!\n\nSizning buyurtmangiz qabul qilindi.\n\nTafsilotlar:\n{order_id}\n\nXaridingiz uchun rahmat!"
    
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [customer_email]
    
    # Email yuborish
    send_mail(subject, message, email_from, recipient_list)
    return f"Order {order_id} uchun email yuborildi."