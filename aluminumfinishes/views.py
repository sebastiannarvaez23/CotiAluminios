from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy
from glasstype.models import GlassType
from aluminumfinishes.models import AluminumFinishes

# Create your views here.
@method_decorator(login_required, name='dispatch') 
class AluminumFinishesTemplateView(TemplateView):
    template_name = "aluminum_finishes.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['aluminum_finishes'] = AluminumFinishes.objects.all()
        return context