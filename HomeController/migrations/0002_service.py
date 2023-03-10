# Generated by Django 4.1.2 on 2022-10-25 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomeController', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='service title')),
                ('description', models.TextField(verbose_name='description')),
                ('image', models.ImageField(upload_to=None, verbose_name='service image')),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Services',
            },
        ),
    ]
