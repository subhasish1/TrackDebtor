# Generated by Django 2.2.1 on 2019-05-19 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organisations', '0009_auto_20190510_1513'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orgid', models.CharField(max_length=3)),
                ('brand', models.CharField(max_length=100)),
                ('quantity', models.CharField(max_length=10)),
                ('price', models.CharField(max_length=20)),
                ('gst', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'product',
            },
        ),
    ]
