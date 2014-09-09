from django.http import HttpResponse,Http404
from django.shortcuts import render, get_object_or_404

from training.models import Athlete

def index(request, athlete_name=None):
    if athlete_name:
        return HttpResponse('Hi {}! Let\'s work on that body!?'.format(athlete_name))
    else:
        return HttpResponse('Hello there! Let\'s do some push ups?')

def get_athletes_list(request):
    athletes_list = Athlete.objects.order_by('name')
    return render(request, 'training/team.html', {'athletes_list': athletes_list})

def get_athlete(request, athlete_id):
    athlete = get_object_or_404(Athlete, pk=athlete_id)
    activities = athlete.last_activities()
    return render(request, 'training/athlete.html', {'athlete': athlete, 'activities_list': activities})