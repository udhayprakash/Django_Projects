# Generated by Django 3.0.4 on 2020-03-30 18:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Customers', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customerdetails',
            old_name='data_of_birth',
            new_name='date_of_birth',
        ),
    ]