from django.db import models

# Create your models here.


class Product_Category(models.Model):
    Category_name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'PRODUCT_CATEGORY'
        ordering = ['Category_name']

    def __str__(self):
        return self.Category_name


class Batch(models.Model):
    batch_no = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'BATCH'

    def __str__(self):
        return self.batch_no


class Product(models.Model):
    product_title = models.CharField(max_length=100)
    product_category = models.ForeignKey(Product_Category, on_delete=models.CASCADE, null=True)
    Product_description = models.TextField()
    Product_name = models.CharField(max_length=100)
    price = models.FloatField(blank=True)
    image = models.ImageField(upload_to='photos = ')
    discount_price = models.FloatField(blank=True, null=True)
    label = models.CharField(max_length=50)
    batch_info = models.ForeignKey(Batch, on_delete=models.CASCADE, blank=True,  null=True)
    PRODUCT_SIZE = (
        ('XS', 'ExtraSmall'),
        ('s', 'small'),
        ('m', 'medium'),
        ('l', 'large'),
        ('xl', 'ExtraLarge'),
        ('xxl', 'VeryLarge'),


    )
    Product_Size = models.CharField(max_length=10, choices=PRODUCT_SIZE, blank=True, null=True)

    def __str__(self):
        return self.product_title

    class Meta:
        verbose_name_plural = 'PRODUCTS'
        ordering = ['product_title']


class Manufacturer(models.Model):

    Manufacturer_name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'MANUFACTURER'
        ordering = ['Manufacturer_name']

    def __str__(self):
        return self.Manufacturer_name


class Sku(models.Model):

    manufacturer_name = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, blank=True, null=True)
    description = models.CharField(max_length=100)
    material = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    packaging_date = models.DateTimeField()
    expiry_date = models.DateTimeField()
    product_info = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:

        verbose_name_plural = 'SKU'
        ordering = ['manufacturer_name']

    def __str__(self):
        return self.description










