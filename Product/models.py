from django.db import models

# Create your models here.
import os
from django.shortcuts import reverse

STATUS = (
    (0, 'Product Finished'),
    (1, 'Product Available')
)

'''def user_directory_path(instance, filename):
     file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    instance.filename=instance.SubjectContent.chapter
    return 'Product/static/images/{0}/{1}'.format(instance.Product.productname, instance.filename)
     
def product_image_name(instance, filename, Product):
        ext = filename.split('.')[-1]
        filename = "%s_%s.%s" % (instance.Product.title, instance.Product.id, ext)
        return os.path.join('images', filename)

'''


# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return str(self.category)


class SubCategory(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    subcategory = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.category}:{self.subcategory}'


class Product(models.Model):
    category = models.ForeignKey(
        'Category', on_delete=models.CASCADE)
    subcategory = models.ForeignKey('Subcategory', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=230)
    status = models.IntegerField(choices=STATUS, default=1)
    image = models.ImageField(upload_to='media/')
    size = models.CharField(max_length=4)
    quantity = models.IntegerField()
    description = models.TextField()
    productstory = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField()
    discount_price = models.IntegerField(blank=True, null=True)



    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Product:detail", kwargs={'slug': self.slug})
