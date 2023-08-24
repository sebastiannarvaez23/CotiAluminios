import factory

from apps.stylewindow.models import StyleWindow

class StyleWindowFactory(factory.django.DjangoModelFactory):
    
    class Meta:
        model = StyleWindow

    name = "O"