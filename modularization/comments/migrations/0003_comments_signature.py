# Generated by Django 4.1.1 on 2022-09-23 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_comments_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='signature',
            field=models.CharField(default='Signature', max_length=100),
        ),
    ]
