# Generated by Django 5.0 on 2024-01-16 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomm_app', '0005_cart_qty'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='order_id',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
