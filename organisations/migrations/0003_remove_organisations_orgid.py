# Generated by Django 2.1.5 on 2019-04-25 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organisations', '0002_organisations_orgpassword'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organisations',
            name='orgid',
        ),
    ]
