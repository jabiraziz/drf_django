# Generated by Django 4.1.2 on 2022-11-17 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_supplier_shops_detail_supplier_shopdetailll'),
    ]

    operations = [
        migrations.RenameField(
            model_name='supplier',
            old_name='shopdetailll',
            new_name='shopdetail',
        ),
    ]
