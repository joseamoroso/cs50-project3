# Generated by Django 2.2 on 2019-05-02 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20190502_0006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='options',
            field=models.CharField(default='', max_length=512),
        ),
    ]
