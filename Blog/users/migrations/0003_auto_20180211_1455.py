# Generated by Django 2.0.2 on 2018-02-11 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20180210_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='image',
            field=models.ImageField(default='http://127.0.0.1:8000/static/img/man.png', upload_to='static/img'),
        ),
    ]
