from django.db import models


# Create your models here.
class Mobiles(models.Model):
    mobile_name = models.CharField(max_length=120, unique=True)
    mobile_brand = models.CharField(max_length=80)
    price = models.PositiveIntegerField()
    number_of_pieces = models.PositiveIntegerField()
    images=models.ImageField(upload_to="images",null=True)

    def __str__(self):
        return self.mobile_name
