# Generated by Django 3.2.4 on 2021-07-01 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_review_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='book_id',
            field=models.IntegerField(default=1),
        ),
    ]
