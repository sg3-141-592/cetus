# Generated by Django 3.1.1 on 2020-09-15 22:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cetus3pur', '0005_auto_20200915_2305'),
    ]

    operations = [
        migrations.AddField(
            model_name='eab_approval',
            name='request',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='cetus3pur.eab_request'),
        ),
    ]