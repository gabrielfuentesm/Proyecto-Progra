# Generated by Django 2.2.4 on 2020-07-08 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miweb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='sintomas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=2)),
                ('email', models.CharField(max_length=2)),
                ('edad', models.CharField(max_length=2)),
                ('fiebre', models.CharField(max_length=2)),
                ('tos', models.CharField(max_length=2)),
                ('cansancio', models.CharField(max_length=2)),
                ('aire', models.CharField(max_length=2)),
                ('pecho', models.CharField(max_length=2)),
                ('cabeza', models.CharField(max_length=2)),
                ('respirar', models.CharField(max_length=2)),
            ],
        ),
    ]