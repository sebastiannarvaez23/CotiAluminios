from django.urls import path
from window import views

urlpatterns = [
    path('', views.QuoteWindow.as_view(), name='quote'),
    path('quote/', views.getQuoteWindow, name="quotewindow"),
]