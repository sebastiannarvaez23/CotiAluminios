from django.urls import path
from quote import views

urlpatterns = [
    path('quote/', views.getQuoteWindow, name="windowquote"),
]