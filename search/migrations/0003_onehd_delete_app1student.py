# Generated by Django 5.0.6 on 2025-02-13 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_app1student_authgroup_authgrouppermissions_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Onehd',
            fields=[
                ('sn', models.IntegerField(primary_key=True, serialize=False)),
                ('movie_name', models.CharField(blank=True, max_length=255, null=True)),
                ('movie_link', models.CharField(blank=True, max_length=355, null=True)),
            ],
            options={
                'db_table': 'onehd',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='App1Student',
        ),
    ]
