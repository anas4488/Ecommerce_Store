# Generated by Django 3.1.4 on 2021-07-05 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20210705_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbase',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='email_address'),
        ),
        migrations.AlterField(
            model_name='userbase',
            name='user_name',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
