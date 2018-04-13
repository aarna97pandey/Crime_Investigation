# Generated by Django 2.0.2 on 2018-04-13 09:08

import UI.models
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='facedatabase',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to=UI.models.content_file_name)),
                ('name', models.CharField(max_length=264)),
                ('crime', models.CharField(max_length=264)),
                ('dob', models.DateField()),
                ('dod', models.DateField()),
                ('Injail', models.CharField(max_length=264)),
                ('gang', models.CharField(max_length=264)),
                ('address', models.CharField(max_length=264)),
            ],
        ),
    ]
