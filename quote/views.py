import json, locale

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect, HttpResponse, FileResponse
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from glasstype.models import GlassType
from aluminumfinishes.models import AluminumFinishes
from stylewindow.models import StyleWindow
from quote.models import MasterArticlesAndServices
from django.views.generic import View
from django.urls import reverse_lazy
from quote.reports.documentquote import export_quote_pdf

# Create your views here.
class QuoteWindowTemplateView(TemplateView):
    template_name = "window-quote.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['style_window'] = StyleWindow.objects.all()
        context['aluminum_finishes'] = AluminumFinishes.objects.all()
        context['glass_type'] = GlassType.objects.all()
        return context

@method_decorator(login_required, name='dispatch')
class ArticlesAndServicesTemplateView(TemplateView):
    template_name = "articles-and-services.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles_and_services'] = MasterArticlesAndServices.objects.all()
        return context

@method_decorator(login_required, name='dispatch')
class ArticlesAndServicesCreateView(CreateView):
    model = MasterArticlesAndServices
    template_name = "articles-and-services.html"
    fields = ['name', 'price']
    
    def get_success_url(self):
        return reverse_lazy('articlesandservices')
    
    def form_valid(self, form):
        name = self.request.POST.get('name')
        price = self.request.POST.get('price')
        # Pendiente terminar esta validación
        if name == None or price == None: return HttpResponse(status=400)
        article_or_service = MasterArticlesAndServices(name=name, price=price)
        article_or_service.save()
        return HttpResponseRedirect(redirect_to=self.get_success_url())

@method_decorator(login_required, name='dispatch')
class ArticlesAndServicesUpdateView(UpdateView):
    model = MasterArticlesAndServices
    template_name = "articles-and-services-update.html"
    fields = ['name', 'price']
    
    def get_success_url(self):
        return reverse_lazy('articlesandservices')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        return response

@method_decorator(login_required, name='dispatch')
class ArticlesAndServicesDeleteView(DeleteView):
    model = GlassType
    template_name = 'articles-and-services-delete.html'
    success_url = reverse_lazy('articlesandservices')

def download_quote(request):
    data = json.loads(request.body)
    document_header = data['documentHeader']
    document_line = data['documentLine']
    document = export_quote_pdf(document_header, document_line)

    filename = "Cotización.pdf"
    response = HttpResponse(document, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="' + filename + '"'
    return response

@csrf_exempt
def getWindowStyles(request):
    styles_window = StyleWindow.objects.all()
    styles_window = list(styles_window.values())
    print(styles_window)
    return JsonResponse({'styles_window': styles_window})

@csrf_exempt
def getAluminumFinishes(request):
    aluminum_finishes = AluminumFinishes.objects.all()
    aluminum_finishes = list(aluminum_finishes.values())
    print(aluminum_finishes)
    return JsonResponse({'aluminum_finishes': aluminum_finishes})

@csrf_exempt
def getTypeGlass(request):
    type_glass = GlassType.objects.all()
    type_glass = list(type_glass.values())
    print(type_glass)
    return JsonResponse({'type_glass': type_glass})

@csrf_exempt
def getQuoteWindow(request):

    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

    # Recepcion de informacion

    data = json.loads(request.body)
    window_style = data['window_style']
    window_width = data['window_width']
    window_height = data['window_height']
    aluminum_finishes = data['aluminum_finishes']
    type_glass = data['type_glass']
    is_glass_frosted = bool(data['glass_frosted'])
    num_window_quote = data['num_window_quote']

    # Validaciones de campos nulos o vacios

    if window_width == '' or window_width == None: return JsonResponse({'status_code': 400, 'result': 0, 'message': 'Ingrese un ancho de ventana'})
    if window_height == '' or window_height == None: return JsonResponse({'status_code': 400, 'result': 0, 'message': 'Ingrese un alto de la ventana'})
    if window_style == '' or window_style == None: return JsonResponse({'status_code': 400, 'result': 0, 'message': 'Seleccione un estilo de ventana'})
    if aluminum_finishes == '' or aluminum_finishes == None: return JsonResponse({'status_code': 400, 'result': 0, 'message': 'Seleccione un acabado en aluminio'})
    if type_glass == '' or type_glass == None: return JsonResponse({'status_code': 400, 'result': 0, 'message': 'Seleccione un tipo de vidrio'})
    if is_glass_frosted == '' or is_glass_frosted == None: return JsonResponse({'status_code': 400, 'result': 0, 'message': 'Indique si desea el vidrio esmerilizado'})
    if num_window_quote == '' or num_window_quote == None: return JsonResponse({'status_code': 400, 'result': 0, 'message': 'Ingrese el numero de unidades a cotizar'})

    # Transformacion de tipos

    window_width = float(window_width)
    window_height = float(window_height)
    num_window_quote = int(num_window_quote)

    # Obtencion de objetos

    window_style = StyleWindow.objects.get(id=window_style)
    aluminum_finishes =  AluminumFinishes.objects.get(id=aluminum_finishes)
    glass_type =  GlassType.objects.get(id=type_glass)
    glass_frosted_price = float(MasterArticlesAndServices.objects.get(name='Esmerilizado').price)
    lock_price = float(MasterArticlesAndServices.objects.get(name='Chapa').price)
    corner_price = float(MasterArticlesAndServices.objects.get(name='Esquina').price)
    num_ship = len(window_style.name)

    # Obtencion de Costos

    aluminum_measures = (2 * window_width * 0.01 + 2 * window_height * 0.01) - (4 * 0.06)
    glass_measures = (window_width - 3) * (window_height - 3)
    aluminum_cost = aluminum_measures * (num_ship) * float(aluminum_finishes.price)
    
    # Esmirilizado
    
    if is_glass_frosted:
        glass_cost = glass_measures * float(glass_type.price) + glass_frosted_price
    else:
        glass_cost = glass_measures * float(glass_type.price)

    # Chapas

    num_lock = window_style.name.count('X')
    if num_lock > 1:
        lock_price = window_style.name.count('X') * lock_price
    else:
        lock_price = 0
    
    # Esquinas

    corners_cost = corner_price * 4 * len(window_style.name)
    unit_cost = (float(lock_price) + float(glass_cost) + float(corners_cost) + float(aluminum_cost))
    total_cost = (float(lock_price) + float(glass_cost) + float(corners_cost) + float(aluminum_cost)) * num_window_quote
    total_cost_format = locale.currency(total_cost, grouping=True, symbol=True)
    data = {
        'name': window_style.name,
        'quantity': num_window_quote,
        'price_unit': unit_cost,
        'price': total_cost,
        'result': total_cost_format
    }

    return JsonResponse({'status_code': 200, 'data': data})



