from django.urls import path
from stylewindow import views

urlpatterns = [
    # Templates
    path('list/', views.StylesWindowTemplateView.as_view(), name="windowstyles"),
    path('create/', views.StylesWindowCreateView.as_view(), name="windowstylescreate"),
    path('delete/<int:pk>/', views.StylesWindowDeleteView.as_view(), name="windowstylesdelete"),
]