# Generated by Django 3.0 on 2019-12-29 06:55

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DBers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='account_type',
            field=models.CharField(choices=[('Staff', 'Staff'), ('DBer', 'DBer')], default='DBer', max_length=5),
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Staff', to='DBers.City')),
                ('state', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Staff', to='DBers.State')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Staff', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DBer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aadhaar', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(12), django.core.validators.MaxValueValidator(12)])),
                ('dob', models.DateField()),
                ('gender', models.CharField(choices=[('Female', 'Female'), ('Male', 'Male')], max_length=6)),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='DBers', to='DBers.City')),
                ('state', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='DBers', to='DBers.State')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='DBer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cities', to='DBers.State'),
        ),
    ]
