from django.urls import path
from apps.aluminumfinishes import views

urlpatterns = [
    path('list/', views.AluminumFinishesTemplateView.as_view(), name="aluminumfinishes"),
    path('create/', views.AluminumFinishesCreateView.as_view(), name="aluminumfinishescreate"),
    path('update/<int:pk>/', views.AluminumFinishesUpdateView.as_view(), name='aluminumfinishesupdate'),
    path('delete/<int:pk>/', views.AluminumFinishesDeleteView.as_view(), name="aluminumfinishesdelete"),
]