from django.urls import path
from authentication import views

urlpatterns = [
    path('login/', views.LoginTemplateView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('users/', views.UsersTemplateView.as_view(), name='users'),
    path('create/', views.UserCreateView.as_view(), name="usercreate"),
    path('delete/<int:pk>/', views.UserDeleteView.as_view(), name="userdelete"),
]