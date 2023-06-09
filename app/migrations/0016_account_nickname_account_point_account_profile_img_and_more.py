# Generated by Django 4.1.5 on 2023-05-09 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_remove_myuser_age_remove_myuser_gender_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='nickname',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='point',
            field=models.IntegerField(max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='profile_img',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='account',
            name='step',
            field=models.IntegerField(max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='age',
            field=models.IntegerField(null=True),
        ),
    ]
