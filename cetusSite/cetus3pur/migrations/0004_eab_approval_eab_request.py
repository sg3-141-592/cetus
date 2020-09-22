# Generated by Django 3.1.1 on 2020-09-15 21:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cetus3pur', '0003_rrresponsiblemanager_user_ac'),
    ]

    operations = [
        migrations.CreateModel(
            name='EAB_Approval',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Date of Review.')),
                ('approver_userid', models.CharField(max_length=10)),
                ('decision', models.CharField(max_length=10)),
                ('ecm_comment', models.CharField(max_length=512)),
                ('ipm_comment', models.CharField(max_length=512)),
                ('IT_comment', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='EAB_Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Date of Req.')),
                ('reqstr_userid', models.CharField(max_length=10)),
                ('data_store', models.CharField(max_length=256)),
                ('data_owner_userid', models.CharField(max_length=10)),
                ('data_store_export_claim', models.CharField(max_length=512)),
                ('ipecr', models.IntegerField()),
                ('tp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cetus3pur.thirdparty')),
            ],
        ),
    ]