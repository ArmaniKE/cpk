# Generated by Django 5.1.6 on 2025-02-17 08:11

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_item_lovers_alter_subcategory_category'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='lovers',
            field=models.ManyToManyField(related_name='favourite_items', to=settings.AUTH_USER_MODEL),
        ),
    ]
