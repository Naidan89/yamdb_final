# Generated by Django 2.2.16 on 2022-05-13 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20220513_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.TextField(blank=True, null=True, verbose_name='Пароль'),
        ),
    ]
