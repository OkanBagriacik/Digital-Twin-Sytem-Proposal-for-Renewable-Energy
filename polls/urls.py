from django.urls import path

from djangoProject import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('report/', views.report, name='report'),
    path('presentation/', views.presentation, name='presentation'),
    path('graphs/', views.graphs, name='graphs'),
    path('declaration/', views.declaration, name='declaration'),
    path('dataRep/', views.dataRep, name='dataRep'),
    path('speResults/', views.speResults, name='speResults'),] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



