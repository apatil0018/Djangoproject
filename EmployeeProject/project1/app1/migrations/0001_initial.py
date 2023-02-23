# Generated by Django 4.1 on 2022-09-04 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('regid', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=50)),
                ('phoneNo', models.CharField(max_length=12)),
                ('photo', models.ImageField(upload_to='image/')),
            ],
        ),
        migrations.CreateModel(
            name='Workexp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cmp_name', models.CharField(max_length=100)),
                ('fromdate', models.DateField()),
                ('todate', models.DateField()),
                ('address', models.CharField(max_length=200)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workexp', to='app1.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Qualification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualificationName', models.CharField(max_length=100)),
                ('fromdate', models.DateField()),
                ('todate', models.DateField()),
                ('percentage', models.FloatField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='qualifications', to='app1.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='app1.employee')),
            ],
        ),
        migrations.CreateModel(
            name='AddressDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('h_no', models.IntegerField()),
                ('street', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='addressDetails', to='app1.employee')),
            ],
        ),
    ]
