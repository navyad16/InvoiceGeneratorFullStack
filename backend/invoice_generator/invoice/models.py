from django.db import models

# Create your models here.

class Invoice(models.Model):
    client_name = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    item = models.CharField(max_length=100)
    quantity = models.IntegerField()
    rate = models.FloatField()

    def total(self):
        return self.quantity * self.rate

