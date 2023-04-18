from django.urls import path
from aluminumfinishes import views

urlpatterns = [
    path('list/', views.AluminumFinishesTemplateView.as_view(), name="aluminumfinishes"),
]