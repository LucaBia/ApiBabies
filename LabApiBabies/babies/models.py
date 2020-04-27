from django.db import models

# Create your models here.

class Baby(models.Model):
    # id creado por defecto
    name = models.CharField(max_length=30, null=False, blank=False)
    lastname = models.CharField(max_length=50, null=False, blank=False)
    parent = models.ForeignKey('parents.Parent', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name + self.lastname