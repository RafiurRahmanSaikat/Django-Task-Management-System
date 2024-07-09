from django.db import models


# Create your models here.


class CategoryModel(models.Model):
    categoryName = models.CharField(max_length=100)

    def __str__(self):
        return self.categoryName
