# Generated by Django 4.1.2 on 2022-10-25 07:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CourierController', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extrapackageinfo',
            name='package',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='extraPackInfo', to='CourierController.package'),
        ),
        migrations.AlterField(
            model_name='package',
            name='percel_type',
            field=models.CharField(choices=[('normal goods', 'Normal goods'), ('express goods', 'Express goods'), ('sengzen goods', 'Shengzen goods')], max_length=100, null=True, verbose_name='parcel type'),
        ),
    ]