# Generated by Django 4.1.3 on 2022-11-22 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CourierController', '0013_rename_customer_name_package_reciever_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='number_of',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='parcel',
            name='number_of',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
