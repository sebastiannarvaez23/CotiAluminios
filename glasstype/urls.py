from django.urls import path
from glasstype import views

urlpatterns = [
    # Templates
    path('list/', views.GlassTypeTemplateView.as_view(), name="glasstype"),
]