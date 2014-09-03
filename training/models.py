from django.db import models

class Athlete(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Activity(models.Model):
    athlete = models.ForeignKey(Athlete)
    sport = models.CharField(max_length=20)
    description = models.CharField(max_length=1000)
    date = models.DateField()

    def __str__(self):
        return '{}: {}'.format(self.date,self.description)