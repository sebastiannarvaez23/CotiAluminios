from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView
from glasstype.models import GlassType

# Create your views here.
@method_decorator(login_required, name='dispatch')
class GlassTypeTemplateView(TemplateView):
    template_name = "glass_type.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['glasses_types'] = GlassType.objects.all()
        return context