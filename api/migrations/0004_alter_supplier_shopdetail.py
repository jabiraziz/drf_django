# Generated by Django 4.1.2 on 2022-11-17 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rename_shopdetailll_supplier_shopdetail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='shopdetail',
            field=models.ManyToManyField(null=True, related_name='shop_detail', to='api.shop'),
        ),
    ]
