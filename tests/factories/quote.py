import factory

from apps.quote.models import MasterArticlesAndServices

class MasterServiceGlassFrostedFactory(factory.django.DjangoModelFactory):
    
    class Meta:
        model = MasterArticlesAndServices

    name = "Esmerilizado"
    price =  5.20

class MasterArticleLockFactory(factory.django.DjangoModelFactory):
    
    class Meta:
        model = MasterArticlesAndServices

    name = "Chapa"
    price =  16200

class MasterArticleCornerFactory(factory.django.DjangoModelFactory):
    
    class Meta:
        model = MasterArticlesAndServices

    name = "Esquina"
    price =  4310