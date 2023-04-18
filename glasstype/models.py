from django.db import models

# Create your models here.
class GlassType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=254, unique=True, verbose_name="Tipo de vidrio")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")

    class Meta:
        verbose_name = "Tipo de vidrio"
        verbose_name_plural = "Tipos de vidrio"
        ordering = ['-id']

    def __str__(self):
        return self.name