# Generated by Django 4.1 on 2022-09-14 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smwapp', '0004_alter_likes_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likes',
            name='has_liked',
            field=models.BooleanField(default=False),
        ),
    ]