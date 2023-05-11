from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy
from .models import StyleWindow

# Create your views here.
@method_decorator(login_required, name='dispatch')
class StylesWindowTemplateView(TemplateView):
    template_name = "window-styles.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['styles_window'] = StyleWindow.objects.all()
        return context
    
@method_decorator(login_required, name='dispatch')
class StylesWindowCreateView(CreateView):
    model = StyleWindow
    template_name = "window-styles.html"
    fields = ['name']
    
    def get_success_url(self):
        return reverse_lazy('windowstyles')
    
    def form_valid(self, form):
        name = self.request.POST.get('name')
        if name == None: return HttpResponse(status=400)
        style_window = StyleWindow(name=name)
        style_window.save()

        return HttpResponseRedirect(redirect_to=self.get_success_url())

@method_decorator(login_required, name='dispatch')
class StylesWindowDeleteView(DeleteView):
    model = StyleWindow
    template_name = 'window-style-conf-delete.html'
    success_url = reverse_lazy('windowstyles')