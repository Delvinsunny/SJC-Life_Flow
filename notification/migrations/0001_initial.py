# Generated by Django 3.2.23 on 2024-01-31 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('notification_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('notification', models.CharField(max_length=150)),
                ('time', models.TimeField()),
            ],
            options={
                'db_table': 'notification',
                'managed': False,
            },
        ),
    ]
