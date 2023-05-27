# Generated by Django 4.1.6 on 2023-02-23 19:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InfoContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='ایمیل')),
                ('address', models.CharField(max_length=110, verbose_name='آدرس من')),
                ('phone', models.CharField(max_length=110, validators=[django.core.validators.RegexValidator('09([0-9][0-9]|3[1-9]|2[1-9])-?[0-9]{3}-?[0-9]{4}', message='لطفا شناره تلفن صحیح وارد کنید شماره تلفن شما اشتباه است دوست من ')])),
            ],
            options={
                'verbose_name': 'اطلاعات تماس',
                'verbose_name_plural': 'اطلاعات تماس',
            },
        ),
    ]