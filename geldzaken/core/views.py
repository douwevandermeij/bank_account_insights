import json
from django.http import HttpResponse
from django.views.generic import TemplateView, View
from geldzaken.core.models import Boeking, Categorie
from geldzaken.core.utils import get_boekingen


class RequestContextTemplateView(TemplateView):

    def get_context_data(self, request, **kwargs):
        return super(RequestContextTemplateView, self).get_context_data(**kwargs)

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(request, *args, **kwargs)
        return self.render_to_response(context)


class YearView(RequestContextTemplateView):
    template_name = 'chart.html'

    def get_context_data(self, request, **kwargs):
        context = super(YearView, self).get_context_data(request, **kwargs)

        context['year'] = int(kwargs['year']) if 'year' in kwargs else 0
        context['month'] = 0
        return context


class DetailView(View):

    def get(self, request, *args, **kwargs):
        boekingen, dateformat = get_boekingen(request, **kwargs)
        return HttpResponse(json.dumps(boekingen),mimetype='application/json')


class BoekingView(View):

    def get(self, request, *args, **kwargs):
        data = {}
        boekingen, dateformat = get_boekingen(request, **kwargs)

        for b in boekingen:
            date_str = b.datum.strftime(dateformat)
            if date_str not in data:
                data[date_str] = {}
            if b.cat().id not in data[date_str]:
                data[date_str][b.cat().id] = 0.0
            data[date_str][b.cat().id] += b.netto()
        return HttpResponse(json.dumps(data),mimetype='application/json')


class CategorieView(View):

    def get(self, request, *args, **kwargs):
        data = [[c.id, c.naam] for c in Categorie.objects.all()]
        return HttpResponse(json.dumps(data),mimetype='application/json')
