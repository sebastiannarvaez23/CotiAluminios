import json

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy
from glasstype.models import GlassType

# Create your views here.
@method_decorator(login_required, name='dispatch')
class GlassTypeTemplateView(TemplateView):
    template_name = "glass_type.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['glasses_types'] = GlassType.objects.all()
        return context