# Generated by Django 2.2 on 2019-06-26 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20190625_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='subscription',
            field=models.CharField(editable=False, max_length=8),
        ),
    ]
