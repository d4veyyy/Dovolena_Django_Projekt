from django.views.generic import DetailView, ListView
from .models import Ucastnik, Dovolena, Flight, Rezervace, Recenze


class UcastnikListView(ListView):
    model = Ucastnik
    template_name = 'ucastnik/ucastnik_detail.html'
    context_object_name = 'ucastnici'


class UcastnikDetailView(DetailView):
    model = Ucastnik
    template_name = 'ucastnik/ucastnik_detail.html'
    context_object_name = 'ucastnik'


class DovolenaListView(ListView):
    model = Dovolena
    template_name = 'dovolena/dovolena_list.html'
    context_object_name = 'dovolene'


class DovolenaDetailView(DetailView):
    model = Dovolena
    template_name = 'dovolena/dovolena_detail.html'
    context_object_name = 'dovolena'


class FlightListView(ListView):
    model = Flight
    template_name = 'flight/flight_list.html'
    context_object_name = 'flights'


class FlightDetailView(DetailView):
    model = Flight
    template_name = 'flight/flight_detail.html'
    context_object_name = 'flight'


class RezervaceListView(ListView):
    model = Rezervace
    template_name = 'rezervace/rezervace_list.html'
    context_object_name = 'rezervace'


class RezervaceDetailView(DetailView):
    model = Rezervace
    template_name = 'rezervace/rezervace_detail.html'
    context_object_name = 'rezervace'


class RecenzeListView(ListView):
    model = Recenze
    template_name = 'recenze/recenze_list.html'
    context_object_name = 'recenze'


class RecenzeDetailView(DetailView):
    model = Recenze
    template_name = 'recenze/recenze_detail.html'
    context_object_name = 'recenze'
