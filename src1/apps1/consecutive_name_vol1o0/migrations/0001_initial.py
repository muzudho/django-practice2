# Generated by Django 3.2.14 on 2022-09-04 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('display_name', models.CharField(max_length=32, verbose_name='表示名')),
                ('sort', models.IntegerField(blank=True, default=0, verbose_name='順番')),
            ],
        ),
    ]
