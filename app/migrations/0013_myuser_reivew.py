# Generated by Django 4.1.5 on 2023-05-02 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='reivew',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
