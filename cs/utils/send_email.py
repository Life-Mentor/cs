from secondary.models import EmailVerifyRecord
from django.core.mail import send_mail
import random
import string

def random_str(randomlength=8):
    chars = string.ascii_letters + string.digits
    strcode = ''.join(random.sample(chars,randomlength))
    return strcode

def send_register_email(email,send_type='register'):
    email_record = EmailVerifyRecord()
    code = random_str()
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    if send_type == 'register':
        email_title = 'blog 激活邮件'
        email_body = '点击下面链接激活账号，http://127.0.0.1:8000/users/active/{0}'.format(code)
        send_status = send_mail(email_title, email_body, '959735909@qq.com',[email],fail_silently=False)

        if send_status:
            pass

    elif send_type == 'forget':
        email_title = '找回密码连接'
        email_body = '点击下面链接找回账号，http://127.0.0.1:8000/users/reset/{0}'.format(code)
        send_status = send_mail(email_title, email_body, '959735909@qq.com',[email],fail_silently=False)

        if send_status:
            pass
