# Generated by Django 4.1.2 on 2022-11-17 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supplier',
            name='shops_detail',
        ),
        migrations.AddField(
            model_name='supplier',
            name='shopdetailll',
            field=models.ManyToManyField(null=True, to='api.shop'),
        ),
    ]