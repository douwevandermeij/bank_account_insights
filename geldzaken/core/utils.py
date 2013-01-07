from geldzaken.core.models import Boeking


def get_boekingen(request, **kwargs):
    if int(kwargs['month']) > 0:
        boekingen = Boeking.objects.filter(datum__year=kwargs['year']).filter(datum__month=kwargs['month']).order_by('datum')
        dateformat = '%Y-%m-%d'
    elif int(kwargs['year']) > 0:
        boekingen = Boeking.objects.filter(datum__year=kwargs['year']).order_by('datum')
        dateformat = '%m'
    else:
        boekingen = Boeking.objects.all().order_by('datum')
        dateformat = '%Y'

    if 'cat' in request.GET and int(request.GET['cat']) > 0:
        boekingen = boekingen.filter(cat__=kwargs['cat'])

    return (boekingen, dateformat)