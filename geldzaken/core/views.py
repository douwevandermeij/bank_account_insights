from django.http import HttpResponse
from django.views.generic import TemplateView, View
from geldzaken.core.models import Boeking, Categorie
import json


class RequestContextTemplateView(TemplateView):

    def get_context_data(self, request, **kwargs):
        return super(RequestContextTemplateView, self).get_context_data(**kwargs)

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(request, **kwargs)
        return self.render_to_response(context)


class IndexView(RequestContextTemplateView):
    template_name = 'chart.html'

    def get_context_data(self, request, **kwargs):
        context = super(IndexView, self).get_context_data(request, **kwargs)

        context['years'] = [0]
#        context['years'] = range(2011, 2014)
        context['months'] = [0]
        if 'y' in request.GET:
            context['years'] = [request.GET['y']]
            context['months'] = range(1, 13)

        return context


class BoekingView(View):

    def get(self, request, *args, **kwargs):
        data = {}
        if 'm' in request.GET and request.GET['m'] != '':
            boekingen = Boeking.objects.filter(datum__year=request.GET['y']).filter(datum__month=request.GET['m']).order_by('datum')
            dateformat = '%Y-%m-%d'
        elif 'y' in request.GET and request.GET['y'] != '':
            boekingen = Boeking.objects.filter(datum__year=request.GET['y']).order_by('datum')
            dateformat = '%m'
        else:
            boekingen = Boeking.objects.all().order_by('datum')
            dateformat = '%Y'

        for b in boekingen:
            date_str = b.datum.strftime(dateformat)
            if date_str not in data:
                data[date_str] = {}
            if b.cat().naam not in data[date_str]:
                data[date_str][b.cat().naam] = 0.0
            data[date_str][b.cat().naam] += b.netto()
        return HttpResponse(json.dumps(data),mimetype='application/json')


class CategorieView(View):

    def get(self, request, *args, **kwargs):
        data = [c.naam for c in Categorie.objects.all()]
        return HttpResponse(json.dumps(data),mimetype='application/json')
