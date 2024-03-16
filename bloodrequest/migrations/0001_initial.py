# Generated by Django 3.2.23 on 2024-01-31 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bloodrequest',
            fields=[
                ('blood_id', models.AutoField(primary_key=True, serialize=False)),
                ('group', models.CharField(max_length=45)),
                ('unit', models.CharField(max_length=45)),
                ('hospital', models.CharField(max_length=45)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('status', models.CharField(max_length=45)),
                ('document', models.CharField(max_length=300)),
            ],
            options={
                'db_table': 'bloodrequest',
                'managed': False,
            },
        ),
    ]