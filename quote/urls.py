from django.urls import path
from quote import views

urlpatterns = [
    path('', views.QuoteWindowTemplateView.as_view(), name='quote'),
    path('api/quote/', views.getQuoteWindow),
    path('api/windowstyles/', views.getWindowStyles),
    path('api/aluminumfinishes/', views.getAluminumFinishes),
    path('api/typeglass/', views.getTypeGlass),
]