# Generated by Django 3.2.4 on 2021-07-01 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20210701_1030'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='authors',
            field=models.CharField(default='Unknown', max_length=256),
        ),
    ]
