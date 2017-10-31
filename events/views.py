from django.views import generic
from events.models import Event
from datetime import date


class IndexView(generic.ListView):
    template_name = 'events/events.html'
    context_object_name = 'all_events'

    def get_queryset(self):
        return Event.objects.filter(end__gte=date.today())


class DetailView(generic.DetailView):
    model = Event
    template_name = 'events/details.html'
