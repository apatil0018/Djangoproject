# Generated by Django 4.1 on 2022-09-03 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_projects'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='image',
            field=models.ImageField(default=1, upload_to='image/'),
            preserve_default=False,
        ),
    ]
