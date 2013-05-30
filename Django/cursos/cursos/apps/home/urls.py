from django.conf.urls import patterns, include, url

urlpatterns = patterns('cursos.apps.home.views',
   	url(r'^$', 'index', name='index'),
)