# Generated by Django 5.0.1 on 2024-02-25 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=30)),
                ('lastName', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=50)),
                ('number', models.CharField(max_length=12)),
                ('company', models.CharField(max_length=30)),
                ('message', models.CharField(max_length=500)),
            ],
        ),
    ]