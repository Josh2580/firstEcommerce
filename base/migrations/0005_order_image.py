# Generated by Django 4.1.4 on 2023-01-23 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_remove_shippingaddress_shippingprice'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
