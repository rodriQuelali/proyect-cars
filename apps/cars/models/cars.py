from django.db import models

__all__ = [
    "Car",
]


class Car(models.Model):
    make = models.CharField(max_length=255, blank=False, null=False)
    year = models.IntegerField(null=False, blank=False)
    model = models.CharField(max_length=128, blank=False, null=False)
    speed = models.IntegerField(null=False, blank=False)
    fuel = models.IntegerField(null=False, blank=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=("make", "model"),
                name="%(app_label)s_%(class)s_unique_make_model",
            )
        ]

    def __str__(self) -> str:
        return f"Make: {self.make} - model {self.model}"

    @property
    def general_information(self):
        return f"Year: {self.year} - Speed {self.speed} - Fuel {self.year}"

    @property
    def car_code(self):
        return f"{self.make[:2]}{self.model[:2]}"
