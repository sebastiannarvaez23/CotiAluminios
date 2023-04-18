import json

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy
from glasstype.models import GlassType
from .models import (
    StyleWindow,
    AluminumFinishes,
)

# Create your views here.

class QuoteWindowTemplateView(TemplateView):
    """Class QuoteWindow"""
    template_name = "window_quote.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['style_window'] = StyleWindow.objects.all()
        context['aluminum_finishes'] = AluminumFinishes.objects.all()
        context['glass_type'] = GlassType.objects.all()
        return context

@method_decorator(login_required, name='dispatch')
class StylesWindowTemplateView(TemplateView):
    template_name = "window_styles.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['styles_window'] = StyleWindow.objects.all()
        return context

@method_decorator(login_required, name='dispatch')
class StylesWindowCreateView(CreateView):
    model = StyleWindow
    template_name = "window_styles.html"
    fields = ['name', 'price']
    
    def get_success_url(self):
        return reverse_lazy('windowstyles')
    
    def form_valid(self, form):
        name = self.request.POST.get('name')
        price = self.request.POST.get('price')
        # Pendiente terminar esta validación
        if name == None or price == None: return HttpResponse(status=400)
        style_window = StyleWindow(name=name, price=price)
        style_window.save()

        return HttpResponseRedirect(redirect_to=self.get_success_url())

@method_decorator(login_required, name='dispatch')
class StylesWindowCreateView(DeleteView):
    model = StyleWindow
    template_name = 'window_style_conf_delete.html'
    success_url = reverse_lazy('windowstyles')

@method_decorator(login_required, name='dispatch') 
class AluminumFinishesTemplateView(TemplateView):
    template_name = "aluminum_finishes.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['aluminum_finishes'] = AluminumFinishes.objects.all()
        return context