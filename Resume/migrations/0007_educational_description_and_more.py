# Generated by Django 4.1.6 on 2023-02-17 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Resume', '0006_workexperince_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='educational',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='توضیحات سابقه تحصیلی'),
        ),
        migrations.AlterField(
            model_name='workexperince',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='توضیحات سابقه کاری'),
        ),
    ]