# Generated by Django 3.1.4 on 2020-12-12 19:56

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('message', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chatbox',
            options={'ordering': ['datum']},
        ),
    ]
