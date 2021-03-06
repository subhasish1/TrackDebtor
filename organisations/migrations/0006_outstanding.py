# Generated by Django 2.1.7 on 2019-04-25 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organisations', '0005_auto_20190425_1809'),
    ]

    operations = [
        migrations.CreateModel(
            name='Outstanding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orgid', models.CharField(max_length=3)),
                ('custid', models.CharField(max_length=3)),
                ('bill_no', models.CharField(max_length=20)),
                ('bill_amt', models.CharField(max_length=20)),
                ('due_amt', models.CharField(max_length=10)),
                ('bill_date', models.DateField()),
                ('cleared_on', models.DateField()),
            ],
            options={
                'db_table': 'outstanding',
            },
        ),
    ]
