from django.db import models
from owner.models import Mobiles
from django.contrib.auth.models import User


# Create your models here.
class Cart(models.Model):
    product = models.ForeignKey(Mobiles, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    quantity = models.PositiveIntegerField(default=1)
    options = (
        ("incart", "incart"),
        ("order placed", "order placed"),
        ("cancelled", "cancelled")
    )
    status = models.CharField(max_length=15,choices=options,default="incart")
