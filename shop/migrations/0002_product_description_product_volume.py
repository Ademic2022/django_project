# Generated by Django 4.2.2 on 2023-06-10 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='volume',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
    ]
