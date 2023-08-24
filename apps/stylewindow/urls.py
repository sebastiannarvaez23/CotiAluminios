from django.urls import path
from apps.stylewindow import views

urlpatterns = [
    path('list/', views.StylesWindowTemplateView.as_view(), name="windowstyles"),
    path('create/', views.StylesWindowCreateView.as_view(), name="windowstylescreate"),
    path('update/<int:pk>/', views.StylesWindowUpdateView.as_view(), name='windowstylesupdate'),
    path('delete/<int:pk>/', views.StylesWindowDeleteView.as_view(), name="windowstylesdelete"),
]