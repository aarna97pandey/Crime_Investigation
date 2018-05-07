# Generated by Django 2.0.2 on 2018-05-06 13:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('UI', '0003_auto_20180506_1914'),
    ]

    operations = [
        migrations.AddField(
            model_name='facedatabase',
            name='dod',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='facedatabase',
            name='crimes',
            field=models.CharField(max_length=264),
        ),
    ]
