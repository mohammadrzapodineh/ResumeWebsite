# Generated by Django 4.1.6 on 2023-02-23 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Resume', '0007_educational_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=110, verbose_name=' نام شبکه اجتماعی')),
                ('link', models.URLField(verbose_name='لینک شبکه اجتماعی شما')),
                ('icon', models.CharField(choices=[('fab fa-facebook-f', 'آیکون فیسبوک'), ('fab fa-twitter', 'آیکون توییتر'), ('fab fa-instagram', 'آیکون اینستاگرم'), ('fab fa-youtube', 'آیکون یوتیوب')], max_length=40, verbose_name='آیکون')),
            ],
            options={
                'verbose_name': 'شبکه اجتماعی',
                'verbose_name_plural': 'شبکه های اجتماعی',
            },
        ),
    ]