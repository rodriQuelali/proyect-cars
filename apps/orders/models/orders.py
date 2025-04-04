from django.db import models

__all__ = [
    "Order",
]


class Order(models.Model):
    user = models.ForeignKey(
        "auth_user.User", related_name="orders", on_delete=models.CASCADE
    )
    car = models.ForeignKey(
        "cars.Car", related_name="car_orders", on_delete=models.CASCADE
    )
    amount = models.IntegerField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
