# Generated by Django 4.0.6 on 2022-07-10 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_customuser_send_messages'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='is_activated',
        ),
    ]