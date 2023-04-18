from django.urls import path
from aluminumfinishes import views

urlpatterns = [
    path('list/', views.AluminumFinishesTemplateView.as_view(), name="aluminumfinishes"),
    path('create/', views.StylesWindowCreateView.as_view(), name="aluminumfinishescreate"),
    path('delete/<int:pk>/', views.StylesWindowDeleteView.as_view(), name="aluminumfinishesdelete"),
]