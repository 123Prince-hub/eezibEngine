# Generated by Django 2.2.18 on 2021-12-20 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Domain_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(max_length=50)),
                ('subdomain', models.CharField(max_length=50)),
                ('open_ports', models.CharField(max_length=50)),
                ('used_technology', models.CharField(max_length=50)),
                ('status_code', models.CharField(max_length=50)),
                ('IP', models.CharField(max_length=50)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
