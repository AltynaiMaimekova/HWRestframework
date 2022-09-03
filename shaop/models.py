from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField()
    QR = models.CharField(max_length=100)

    def __str__(self):
        return self.name



