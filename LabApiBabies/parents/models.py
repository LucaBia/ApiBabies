from django.db import models

# Create your models here.

class Parent(models.Model):
    # id creado por defecto
    name = models.CharField(max_length=30, null=False, blank=False)
    lastname = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name + self.lastname
