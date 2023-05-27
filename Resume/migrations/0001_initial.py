# Generated by Django 4.1.6 on 2023-02-10 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=110, verbose_name='title')),
                ('persent', models.IntegerField(default=0, verbose_name='persent')),
            ],
            options={
                'ordering': ['persent'],
            },
        ),
    ]
