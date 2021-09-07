from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

class Item(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, null=True, blank=True, 
        on_delete=models.SET_NULL, related_name="items")
    description = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    price = models.DecimalField(max_digits=25, decimal_places=2)
    owner = models.ForeignKey('auth.User', related_name='items', on_delete=models.CASCADE)

    def __str__(self):
        return self.name