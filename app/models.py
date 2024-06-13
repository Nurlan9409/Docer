from django.db import models
# from django.views import View

class Products(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price=models.IntegerField()




    class Meta:
        db_table = "product"