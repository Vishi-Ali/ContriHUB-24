# Generated by Django 3.2.7 on 2021-10-13 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0036_auto_20211012_1930'),
    ]

    operations = [
        migrations.AddField(
            model_name='pullrequest',
            name='remark',
            field=models.CharField(default='', max_length=50),
        ),
    ]
