from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=64,  blank=True, null=True, default=None)
    description = models.TextField(blank=True, null=True, default=None)
    short_description = models.TextField(blank=True, null=True, default=None)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now_add=False, auto_now=True)

    # красивий вывод в админке
    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class ProductImage(models.Model):
    product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.PROTECT)
    image = models.ImageField(upload_to='static/media/product_image')
    is_active = models.BooleanField(default=True)
    is_mail = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return '{}'.format(self.id)

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фотографии'