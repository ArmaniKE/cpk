from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    image_url = models.CharField(max_length=255)
    parent = models.ForeignKey('self', on_delete=models.RESTRICT, related_name='children', null=True, blank=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        db_table = 'categories'

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'image_url': self.image_url
        }

    def __str__(self):
        return self.name
#
# class Product(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#
#     class Meta:
#         verbose_name = 'Product'
#         verbose_name_plural = 'Products'
#         db_table = 'products'
#
#     def to_json(self):
#         return {
#             'id': self.id,
#             'name': self.name,
#             'description': self.description,
#         }