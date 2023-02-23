# Generated by Django 4.1.7 on 2023-02-18 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.IntegerField()),
                ('fname', models.CharField(max_length=40)),
                ('lname', models.CharField(max_length=40)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=40)),
            ],
        ),
    ]
