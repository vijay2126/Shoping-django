# Generated by Django 3.0.3 on 2020-02-27 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_registermodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterModel1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=100)),
                ('Last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('mobile_no', models.CharField(max_length=10)),
                ('Addresh', models.CharField(max_length=100)),
                ('Password1', models.CharField(max_length=25)),
            ],
        ),
    ]
