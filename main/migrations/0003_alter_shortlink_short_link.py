# Generated by Django 4.0.6 on 2022-07-09 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_shortlink_options_alter_shortlink_date_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortlink',
            name='short_link',
            field=models.CharField(blank=True, max_length=15, verbose_name='Сокращенная ссылка'),
        ),
    ]
