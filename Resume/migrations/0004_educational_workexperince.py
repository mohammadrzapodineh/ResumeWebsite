# Generated by Django 4.1.6 on 2023-02-12 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Resume', '0003_favorite_service_alter_skill_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Educational',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='عنوان سابقه تحصیلی')),
                ('date_joined', models.DateField(verbose_name='تاریخ شروع ')),
                ('date_left', models.DateField(blank=True, null=True, verbose_name='تاریخ پایان')),
                ('college', models.CharField(max_length=110, verbose_name='نام کالج')),
            ],
            options={
                'verbose_name': 'سابقه کاری',
                'verbose_name_plural': 'سوابق کاری',
            },
        ),
        migrations.CreateModel(
            name='WorkExperince',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='عنوان سابقه کاری')),
                ('date_joined', models.DateField(verbose_name='تاریخ شروع کار')),
                ('date_left', models.DateField(blank=True, null=True, verbose_name='تاریخ پایان کار')),
                ('company', models.CharField(max_length=110, verbose_name='شرکت محل کار')),
            ],
            options={
                'verbose_name': 'سابقه کاری',
                'verbose_name_plural': 'سوابق کاری',
            },
        ),
    ]