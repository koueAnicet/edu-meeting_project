# Generated by Django 4.0.6 on 2022-07-05 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Meeting', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meetings',
            name='name',
        ),
        migrations.AlterField(
            model_name='categorymeeting',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]