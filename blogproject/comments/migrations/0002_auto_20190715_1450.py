# Generated by Django 2.2.3 on 2019-07-15 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
