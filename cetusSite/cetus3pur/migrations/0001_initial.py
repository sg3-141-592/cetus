# Generated by Django 3.1.1 on 2020-09-06 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RRResponsibleManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('familyname', models.CharField(max_length=50)),
                ('employee_id', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ThirdParty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('legal_entity_name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ThirdPartyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('familyname', models.CharField(max_length=50)),
                ('employee_id', models.CharField(max_length=20)),
                ('userac_name', models.CharField(max_length=10)),
                ('userac_expirydate', models.DateTimeField(verbose_name='Expiry date')),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cetus3pur.thirdparty')),
            ],
        ),
    ]