from django.db import models

class Athlete(models.Model):
    name = models.CharField(max_length=200)

    def last_registered_activity_date(self):
        last_activity = Activity.objects.filter(athlete=self.id).order_by('-date').first()
        if last_activity:
            return last_activity.date
        else:
            return None
    last_registered_activity_date.short_description = 'Date of last registered activity'

    def last_activities(self, amount=10):
        return Activity.objects.filter(athlete=self.id).order_by('-date')[:amount]

    def __str__(self):
        return self.name

class Activity(models.Model):
    athlete = models.ForeignKey(Athlete)
    sport = models.CharField(max_length=20)
    description = models.CharField(max_length=1000)
    date = models.DateField()

    def last_feedback(self):
        try:
            feedback = ActivityFeedback.objects.get(activity=self.id)
            return feedback.description
        except ActivityFeedback.DoesNotExist:
            return ''

    def __str__(self):
        return '{}: {} - {}'.format(self.date, self.sport, self.description)

class ActivityFeedback(models.Model):
    activity = models.ForeignKey(Activity)
    description = models.CharField(max_length=1000)
    #date = models.DateField()
