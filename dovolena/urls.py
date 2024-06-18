from django.urls import path
from . import views


from django.views.generic import TemplateView

app_name = 'dovolena'

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('dovolena/', views.DovolenaListView.as_view(), name='dovolena_list'),
    path('dovolena/<int:pk>/', views.DovolenaDetailView.as_view(), name='dovolena_detail'),
    path('flight/', views.FlightListView.as_view(), name='flight_list'),
    path('flight/<int:pk>/', views.FlightDetailView.as_view(), name='flight_detail'),
    path('recenze/', views.RecenzeListView.as_view(), name='recenze_list'),
    path('recenze/<int:pk>/', views.RecenzeDetailView.as_view(), name='recenze_detail'),
    path('rezervace', views.RezervaceListView.as_view(), name='rezervace_list'),
    path('rezervace/<int:pk>/', views.RezervaceDetailView.as_view(), name='rezervace_detail'),
    path('ucastnik/', views.UcastnikListView.as_view(), name='ucastnik_list'),
    path('ucastnik/<int:pk>/', views.UcastnikDetailView.as_view(), name='ucastnik_detail'),
]
