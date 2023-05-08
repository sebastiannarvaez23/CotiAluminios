from django.db import models

# Create your models here.
class StyleWindow(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=254, unique=True, verbose_name="Nombre estilo")

    class Meta:
        verbose_name = "Estilo Ventana"
        verbose_name_plural = "Estilos Ventanas"
        ordering = ['-id']

    def __str__(self):
        return self.name