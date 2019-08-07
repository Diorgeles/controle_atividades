# Generated by Django 2.2 on 2019-07-31 00:39

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20190625_2258'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='created',
            field=model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created'),
        ),
        migrations.AddField(
            model_name='activity',
            name='is_removed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='activity',
            name='modified',
            field=model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified'),
        ),
        migrations.AddField(
            model_name='finalgrade',
            name='created',
            field=model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created'),
        ),
        migrations.AddField(
            model_name='finalgrade',
            name='is_removed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='finalgrade',
            name='modified',
            field=model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified'),
        ),
        migrations.AddField(
            model_name='questions',
            name='created',
            field=model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created'),
        ),
        migrations.AddField(
            model_name='questions',
            name='is_removed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='questions',
            name='modified',
            field=model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified'),
        ),
        migrations.CreateModel(
            name='WrongAlternative',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('is_removed', models.BooleanField(default=False)),
                ('response', models.CharField(max_length=100, verbose_name='Resposta')),
                ('alternative', models.CharField(choices=[('a', 'A)'), ('b', 'B)'), ('c', 'C)'), ('d', 'D)')], max_length=50, verbose_name='Alternativa incorreta')),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Activity')),
            ],
            options={
                'verbose_name': 'Alternativa Incorreta',
                'verbose_name_plural': 'Alternativas Incorretas',
            },
        ),
        migrations.AddField(
            model_name='questions',
            name='wrong_alternative',
            field=models.ManyToManyField(to='core.WrongAlternative', verbose_name='Respostas incorretas'),
        ),
    ]
