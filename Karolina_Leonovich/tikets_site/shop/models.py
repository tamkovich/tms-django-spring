from django.db import models


class Order(models.Model):
    customer_name = models.CharField(max_length=255)
    departure = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    quantity = models.IntegerField(default=0)
    date = models.DateField()

    def __str__(self):
        return f"{self.customer_name}: {self.departure}-{self.destination} ({self.quantity})/{self.date}"
