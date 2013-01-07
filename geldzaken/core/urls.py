from django.conf.urls import patterns, include, url
from geldzaken.core import views as core_views

urlpatterns = patterns('',
    url(r'^$', core_views.YearView.as_view(), name='totaal'),
    url(r'^year/(?P<year>\d{4})/', core_views.YearView.as_view(), name='year'),

    url(r'^json/boeking/(?P<year>\d+)/(?P<month>\d+)/', core_views.BoekingView.as_view(), name='boeking'),
    url(r'^json/categorie/', core_views.CategorieView.as_view(), name='categorie'),
    url(r'^json/details/(?P<year>\d+)/(?P<month>\d+)/', core_views.DetailView.as_view(), name='details'),
)
