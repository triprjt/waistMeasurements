from django.db import models

class Measurement(models.Model):
    height = models.DecimalField(max_digits=5, decimal_places=2)
    age = models.DecimalField(max_digits=5, decimal_places=2)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    waist = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f'{self.height}, {self.age}, {self.weight}, {self.waist}'
