# Generated by Django 4.1.5 on 2023-05-23 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_alter_account_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='ballcount',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='picklist',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
