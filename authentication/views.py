from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.urls import reverse
from django.views.generic.base import TemplateView, View

class LoginTemplateView(TemplateView):
    template_name = 'login.html'

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirigir al usuario a la página que estaba tratando de acceder
            return redirect(request.GET.get('next', '/window/'))
        # Si la autenticación falla, mostrar un mensaje de error
        return render(request, self.template_name, {'error_message': 'Nombre de usuario o contraseña incorrectos'})

class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect(reverse('login'))

@method_decorator(login_required, name='dispatch')
class UsersTemplateView(TemplateView):
    template_name = "users.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.all()
        return context