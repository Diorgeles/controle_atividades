# Generated by Django 2.2 on 2019-08-10 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20190810_1414'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='response',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Resposta'),
        ),
    ]