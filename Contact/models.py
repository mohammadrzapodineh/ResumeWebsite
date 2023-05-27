from django.db import models
from .regex_validatos import phone_regex

class InfoContact(models.Model):
    email = models.EmailField(verbose_name='ایمیل')
    address = models.CharField(verbose_name='آدرس من', max_length=110)
    phone = models.CharField(max_length=110, validators=[phone_regex], verbose_name='شماره تماس')


    class Meta:
        verbose_name = 'اطلاعات تماس'
        verbose_name_plural = 'اطلاعات تماس'

    
    def __str__(self):
        return f'اطلاعات تماس برای ایمیل:{self.email}'
