# Generated by Django 3.1.1 on 2020-09-15 22:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cetus3pur', '0009_auto_20200915_2326'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rrresponsiblemanager',
            options={'verbose_name': 'R-R Responsible Manager', 'verbose_name_plural': 'R-R Responsible Managers'},
        ),
        migrations.AlterModelOptions(
            name='thirdparty',
            options={'verbose_name': '3P Business', 'verbose_name_plural': '3P Businesses'},
        ),
        migrations.AlterModelOptions(
            name='thirdpartyuser',
            options={'verbose_name': '3P User', 'verbose_name_plural': '3P Users'},
        ),
    ]