# Generated by Django 3.2.4 on 2021-06-30 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20210630_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='page_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='book',
            name='short_description',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='thumbnail_url',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
