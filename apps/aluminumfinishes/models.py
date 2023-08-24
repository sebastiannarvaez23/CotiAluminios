from django.db import models

# Create your models here.
class AluminumFinishes(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=254, unique=True, verbose_name="Nombre acabado")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")

    class Meta:
        verbose_name = "Acabo ventana"
        verbose_name_plural = "Acabados ventana"
        ordering = ['-id']

    def __str__(self):
        return self.name
    
