# Generated by Django 5.1.6 on 2025-02-16 20:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_cart_options_alter_cartitem_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='items', to='shop.subcategory'),
        ),
    ]
