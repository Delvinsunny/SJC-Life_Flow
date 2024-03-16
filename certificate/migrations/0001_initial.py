# Generated by Django 3.2.23 on 2024-01-31 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('certificate_id', models.AutoField(primary_key=True, serialize=False)),
                ('donated_date', models.DateField()),
                ('certificate', models.CharField(max_length=500)),
                ('hospital', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'certificate',
                'managed': False,
            },
        ),
    ]