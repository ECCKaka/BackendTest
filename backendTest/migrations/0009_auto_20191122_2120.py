# Generated by Django 2.2.7 on 2019-11-23 04:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backendTest', '0008_auto_20191122_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='user',
            field=models.OneToOneField(db_column='userId', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]