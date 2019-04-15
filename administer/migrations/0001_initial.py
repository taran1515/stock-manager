# Generated by Django 2.2 on 2019-04-14 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=40)),
                ('model_no', models.CharField(max_length=10)),
                ('color', models.CharField(blank=True, max_length=20, null=True)),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('supplier', models.CharField(blank=True, max_length=40, null=True)),
                ('date_of_purchase', models.DateField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=40)),
                ('model_no', models.CharField(max_length=10)),
                ('color', models.CharField(blank=True, max_length=20, null=True)),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('retailer', models.CharField(blank=True, max_length=40, null=True)),
                ('date_of_sale', models.DateField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=40)),
                ('model_no', models.CharField(max_length=10)),
                ('color', models.CharField(blank=True, max_length=20, null=True)),
                ('quantity', models.IntegerField()),
            ],
        ),
    ]
