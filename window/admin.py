from django.contrib import admin
from .models import (
    StyleWindow,
    AluminumFinishes,
    GlassType,
)

# Register your models here.
admin.site.register(StyleWindow)
admin.site.register(AluminumFinishes)
admin.site.register(GlassType)