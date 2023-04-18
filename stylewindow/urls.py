from django.urls import path
from stylewindow import views

urlpatterns = [
    # Templates
    path('styles/', views.StylesWindowTemplateView.as_view(), name="windowstyles"),
    path('styles/create/', views.StylesWindowCreateView.as_view(), name="windowstylescreate"),
    path('styles/delete/<int:pk>/', views.StylesWindowDeleteView.as_view(), name="windowstylesdelete"),
]