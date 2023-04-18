from django.urls import path
from glasstype import views

urlpatterns = [
    # Templates
    path('list/', views.GlassTypeTemplateView.as_view(), name="glasstype"),
    path('create/', views.GlassTypeCreateView.as_view(), name="glasstypecreate"),
    path('delete/<int:pk>/', views.GlassTypeDeleteView.as_view(), name="glasstypedelete"),
]