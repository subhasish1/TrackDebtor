# Generated by Django 2.1.5 on 2019-04-25 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organisations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='organisations',
            name='orgpassword',
            field=models.CharField(default=123, max_length=13),
            preserve_default=False,
        ),
    ]
