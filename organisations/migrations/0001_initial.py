# Generated by Django 2.1.5 on 2019-04-25 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organisations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orgid', models.CharField(max_length=3)),
                ('orgname', models.CharField(max_length=50)),
                ('orgemail', models.CharField(max_length=100)),
                ('orgcc', models.CharField(max_length=500)),
                ('orgsendername', models.CharField(max_length=50)),
                ('orgsenderphn', models.CharField(max_length=13)),
            ],
        ),
    ]