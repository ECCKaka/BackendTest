# Generated by Django 2.2.7 on 2019-11-23 06:45

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
            name='Actions',
            fields=[
                ('actionId', models.AutoField(primary_key=True, serialize=False)),
                ('time', models.DateTimeField(null=True)),
                ('type', models.TextField(null=True)),
                ('user', models.ForeignKey(db_column='user', on_delete=django.db.models.deletion.CASCADE, related_name='actions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Actions',
                'db_table': 'Actions',
            },
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sessionId', models.TextField(null=True)),
                ('userId', models.ForeignKey(db_column='userId', on_delete=django.db.models.deletion.CASCADE, related_name='session', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Session',
                'db_table': 'Session',
            },
        ),
        migrations.CreateModel(
            name='Properties',
            fields=[
                ('propertiesId', models.AutoField(primary_key=True, serialize=False)),
                ('pageFrom', models.TextField(null=True)),
                ('pageTo', models.TextField(null=True)),
                ('viewedId', models.TextField(null=True)),
                ('locationX', models.IntegerField(null=True)),
                ('locationY', models.IntegerField(null=True)),
                ('actionId', models.OneToOneField(db_column='actionId', on_delete=django.db.models.deletion.CASCADE, to='backendTest.Actions')),
            ],
            options={
                'verbose_name': 'Properties',
                'db_table': 'Properties',
            },
        ),
    ]
