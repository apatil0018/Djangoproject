# Generated by Django 4.0.3 on 2022-09-03 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_rename_employee_addressdetails_addressdetails'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addressdetails',
            old_name='addressDetails',
            new_name='employee',
        ),
    ]
