# Generated by Django 4.1.6 on 2023-02-17 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Resume', '0005_alter_educational_options_biography_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='workexperince',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='توضیحات خدمات'),
        ),
    ]
