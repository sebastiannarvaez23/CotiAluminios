import factory

from apps.glasstype.models import GlassType

class GlassTypeFactory(factory.django.DjangoModelFactory):
    
    class Meta:
        model = GlassType

    name = "Transparente"
    price =  8.25