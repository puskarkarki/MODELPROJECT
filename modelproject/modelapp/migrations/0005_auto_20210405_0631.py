# Generated by Django 3.1.7 on 2021-04-05 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modelapp', '0004_auto_20210405_0616'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product_category',
            options={'ordering': ['Category_name'], 'verbose_name_plural': 'PRODUCT_CATEGORY'},
        ),
        migrations.RenameField(
            model_name='product_category',
            old_name='name',
            new_name='Category_name',
        ),
    ]
