# Generated by Django 3.2 on 2022-10-28 17:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('job_type', models.CharField(choices=[('Remote', 'Remote'), ('Hyperd', 'Hyperd'), ('On-site', 'On-site')], max_length=19)),
                ('catgory', models.CharField(max_length=15)),
                ('requiremnt', models.TextField(max_length=50)),
                ('salary', models.CharField(max_length=35)),
                ('country', models.CharField(max_length=15)),
                ('description', models.TextField(max_length=50)),
                ('Benefits', models.TextField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('cover_letter', models.TextField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]