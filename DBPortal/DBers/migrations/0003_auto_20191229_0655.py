# Generated by Django 3.0 on 2019-12-29 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DBers', '0002_auto_20191229_0655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='state',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]
