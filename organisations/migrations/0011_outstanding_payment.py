# Generated by Django 2.2.1 on 2019-05-20 07:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('organisations', '0010_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='outstanding',
            name='payment',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
    ]
