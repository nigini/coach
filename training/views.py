from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse

from training.models import Athlete,Activity, ActivityFeedback


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


def feedback(request, athlete_id, activity_id):
    activity = Activity.objects.get(pk=activity_id)
    if activity:
        try:
            feedback_description = request.POST['feedback_text']
            activity_feedback = ActivityFeedback.objects.get(activity=activity)
            if activity_feedback:
                activity_feedback.description = feedback_description
            else:
                activity_feedback = ActivityFeedback(activity=activity, description=feedback_description)
            activity_feedback.save()
            return HttpResponseRedirect(reverse('training:athlete', args=(athlete_id,)))
        except KeyError:
            return render(request, reverse('training:athlete', args=(athlete_id,)), {
                'error_message': 'Strange! Have you provided a feedback text? =/',
                })
    else:
        return render(request, reverse('training:athlete', args=(athlete_id,)), {
            'error_message': 'Strange! Could not find the requested Activity. =[',
        })