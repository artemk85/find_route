# Generated by Django 3.1.7 on 2021-02-28 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0002_auto_20210227_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Город'),
        ),
    ]
