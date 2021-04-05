# Generated by Django 3.1.7 on 2021-04-05 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_title', models.CharField(max_length=100)),
                ('Product_description', models.TextField()),
                ('Product_name', models.CharField(max_length=100)),
                ('price', models.FloatField(blank=True)),
                ('discount_price', models.FloatField(blank=True, null=True)),
                ('label', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('Product_Size', models.CharField(choices=[('XS', 'Extramall'), ('s', 'small'), ('m', 'medium'), ('l', 'large'), ('xl', 'Extralarge'), ('xxl', 'VeryLarge')], max_length=10)),
            ],
        ),
    ]
