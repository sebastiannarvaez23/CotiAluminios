from django.urls import path
from authentication import views

urlpatterns = [
    path('login/', views.LoginTemplateView.as_view(), name='login'),
    path('logout/', views.LogoutTemplateView.as_view(), name='logout'),
]