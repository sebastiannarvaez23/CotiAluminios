import json

from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from glasstype.models import GlassType
from window.models import AluminumFinishes
from stylewindow.models import StyleWindow

# Create your views here.
@csrf_exempt
def getQuoteWindow(request):

    dicTipoVentana = {'O': 1, 'XO': 2, 'OXO': 3, 'OXXO':4}

    data = json.loads(request.body)
    estilo_ventana = data['estilo_ventana']
    ancho = int(data['ancho'])
    alto = int(data['alto'])
    acabado_aluminio = data['acabado_aluminio']
    tipo_vidrio = data['tipo_vidrio']
    vidrio_esmerilado = bool(data['vidrio_esmerilado'])
    numero_ventanas_cotizar = int(data['numero_ventanas_cotizar'])

    aluminum_finishes =  AluminumFinishes.objects.get(id=acabado_aluminio)
    glass_type =  GlassType.objects.get(id=tipo_vidrio)

    floMedidasAluminio = 2*ancho*0.01 + 2*alto*0.01 - 4*0.06
    floMedidasVidrio = (ancho - 3)*(alto - 3)
    floCostoAluminio = floMedidasAluminio*(dicTipoVentana[str(estilo_ventana)])*float(aluminum_finishes.price)
    
    if vidrio_esmerilado:
        floCostoVidrio = floMedidasVidrio*glass_type.price+5.20
    else:
        floCostoVidrio = floMedidasVidrio*glass_type.price

    floCostoChapas = 0

    if dicTipoVentana[str(estilo_ventana)] == 'XO' or dicTipoVentana[str(estilo_ventana)] == 'XO':
        floCostoChapas = 16200
    elif dicTipoVentana[str(estilo_ventana)] == 'OXXO':
        floCostoChapas = 2*16200

    floCostoEsquinas = 4310*4*(dicTipoVentana[str(estilo_ventana)])

    floCostoTotal = (float(floCostoChapas) + float(floCostoVidrio) + float(floCostoEsquinas) + float(floCostoAluminio))*numero_ventanas_cotizar
    if numero_ventanas_cotizar >= 100:
        floCostoTotal = floCostoTotal*(1-0.1)

    return JsonResponse({'result': floCostoTotal})
 
class QuoteWindowTemplateView(TemplateView):
    """Class QuoteWindow"""
    template_name = "window_quote.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['style_window'] = StyleWindow.objects.all()
        context['aluminum_finishes'] = AluminumFinishes.objects.all()
        context['glass_type'] = GlassType.objects.all()
        return context