from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.urls import reverse
from django.views.generic.base import TemplateView, View
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy

class LoginTemplateView(TemplateView):
    template_name = 'login.html'

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirigir al usuario a la página que estaba tratando de acceder
            return redirect(request.GET.get('next', '/'))
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
    
@method_decorator(login_required, name='dispatch')
class UserCreateView(CreateView):
    model = User
    template_name = "users.html"
    fields = [
        'username',
        'first_name',
        'last_name',
        'email',
    ]
    
    def get_success_url(self):
        return reverse_lazy('users')
    
    def form_valid(self, form):
        username = self.request.POST.get('username')
        first_name = self.request.POST.get('firstname')
        last_name = self.request.POST.get('lastname')
        email = self.request.POST.get('email')
        password = self.request.POST.get('password')
        is_staff = self.request.POST.get('isadmin')
        # Pendiente terminar esta validación
        
        user = User(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
        )
        user.set_password(password)
        if is_staff != None: user.is_staff = True
        user.save()
        return HttpResponseRedirect(redirect_to=self.get_success_url())

@method_decorator(login_required, name='dispatch')
class UserDeleteView(DeleteView):
    model = User
    template_name = 'user_conf_delete.html'
    success_url = reverse_lazy('users')