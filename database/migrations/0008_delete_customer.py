# Generated by Django 4.1 on 2022-09-09 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0007_customer_name_alter_customer_first_name_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Customer',
        ),
    ]
