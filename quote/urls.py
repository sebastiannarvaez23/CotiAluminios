from django.urls import path
from quote import views

urlpatterns = [
    path('', views.QuoteWindowTemplateView.as_view(), name='quote'),
    path('articles-and-services/', views.ArticlesAndServicesTemplateView.as_view(), name='articlesandservices'),
    path('articles-and-services-create/', views.ArticlesAndServicesCreateView.as_view(), name='articlesandservicescreate'),
    path('articles-and-services-delete/<int:pk>/', views.ArticlesAndServicesDeleteView.as_view(), name='articlesandservicesdelete'),
    path('api/quote/', views.getQuoteWindow),
    path('api/windowstyles/', views.getWindowStyles),
    path('api/aluminumfinishes/', views.getAluminumFinishes),
    path('api/typeglass/', views.getTypeGlass),
]