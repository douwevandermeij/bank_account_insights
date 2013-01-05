from django.conf.urls import patterns, include, url
from geldzaken.core import views as core_views

urlpatterns = patterns('',
    url(r'^$', core_views.IndexView.as_view(), name='index'),
    url(r'^boeking/', core_views.BoekingView.as_view(), name='boeking'),
    url(r'^categorie/', core_views.CategorieView.as_view(), name='categorie'),
)
