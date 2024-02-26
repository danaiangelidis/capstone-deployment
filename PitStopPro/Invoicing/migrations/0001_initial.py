# Generated by Django 4.2.6 on 2023-12-08 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=30)),
                ('lastName', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=80)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=50)),
                ('type', models.CharField(max_length=30)),
                ('make', models.CharField(max_length=30)),
                ('model', models.CharField(max_length=30)),
                ('year', models.CharField(max_length=30)),
                ('plateNumber', models.CharField(max_length=30)),
                ('laborHours', models.IntegerField()),
                ('laborRate', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('item1Desc', models.TextField()),
                ('item1Price', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('item1Qty', models.IntegerField()),
                ('item2Desc', models.TextField()),
                ('item2Price', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('item2Qty', models.IntegerField()),
                ('item3Desc', models.TextField()),
                ('item3Price', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('item3Qty', models.IntegerField()),
                ('Tax', models.DecimalField(decimal_places=2, max_digits=5)),
                ('totalPrice', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('totalLabor', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('totalItems', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('totalNoTax', models.DecimalField(decimal_places=2, max_digits=1000)),
            ],
        ),
    ]