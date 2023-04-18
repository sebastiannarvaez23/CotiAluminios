from django.urls import path
from window import views

urlpatterns = [
    # Templates
    path('aluminum/', views.AluminumFinishesTemplateView.as_view(), name="aluminumfinishes"),
]