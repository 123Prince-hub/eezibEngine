# Generated by Django 2.2.18 on 2021-12-20 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domain_info', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='domain_info',
            old_name='created_date',
            new_name='date',
        ),
        migrations.RemoveField(
            model_name='domain_info',
            name='IP',
        ),
        migrations.RemoveField(
            model_name='domain_info',
            name='status_code',
        ),
        migrations.RemoveField(
            model_name='domain_info',
            name='used_technology',
        ),
        migrations.AddField(
            model_name='domain_info',
            name='comment',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='domain_info',
            name='directories',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='domain_info',
            name='ip',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='domain_info',
            name='lookup',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='domain_info',
            name='status',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='domain_info',
            name='technology',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='domain_info',
            name='urls',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='domain_info',
            name='domain',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='domain_info',
            name='open_ports',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='domain_info',
            name='subdomain',
            field=models.CharField(max_length=255),
        ),
    ]
