from django.urls import path
from aluminumfinishes import views

urlpatterns = [
    path('list/', views.AluminumFinishesTemplateView.as_view(), name="aluminumfinishes"),
    path('create/', views.AluminumFinishesCreateView.as_view(), name="aluminumfinishescreate"),
    path('delete/<int:pk>/', views.AluminumFinishesDeleteView.as_view(), name="aluminumfinishesdelete"),
]