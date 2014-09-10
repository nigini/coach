import datetime

from django.utils import timezone
from django.test import TestCase

from training.models import Athlete, Activity, ActivityFeedback


class AthleteActivityTests(TestCase):


    def test_no_last_activities(self):
        test_athlete_1 = Athlete(name='Test Athlete')
        self.assertIsNone(test_athlete_1.last_registered_activity_date())
        self.assertEqual(len(test_athlete_1.last_activities()), 0)


    def test_some_last_activities(self):
        test_athlete_1 = Athlete(name='Test Athlete')
        test_athlete_1.save()
        test_date_1 = timezone.now() - datetime.timedelta(days=1)
        test_activity_1 = Activity(athlete=test_athlete_1, sport='test_sport', description='test_description',
                                   date=test_date_1)
        test_activity_1.save()
        self.assertEqual(test_athlete_1.last_registered_activity_date(), test_date_1.date())
        self.assertEqual(len(test_athlete_1.last_activities()), 1)

        test_date_2 = timezone.now() - datetime.timedelta(days=2)
        test_activity_1 = Activity(athlete=test_athlete_1, sport='test_sport', description='test_description',
                                   date=test_date_2)
        test_activity_1.save()
        self.assertEqual(test_athlete_1.last_registered_activity_date(), test_date_1.date())
        test_activities = test_athlete_1.last_activities()
        self.assertEqual(len(test_activities), 2)
        self.assertTrue(test_activities[0].date > test_activities[1].date)


class ActivityFeedbackTests(TestCase):

    def test_no_feedback(self):
        test_athlete_1 = Athlete(name='Test Athlete')
        test_athlete_1.save()
        test_date_1 = timezone.now() - datetime.timedelta(days=1)
        test_activity_1 = Activity(athlete=test_athlete_1, sport='test_sport', description='test_description',
                                   date=test_date_1)
        test_activity_1.save()
        self.assertEqual(test_activity_1.last_feedback(), '')


    def test_some_feedback(self):
        test_athlete_1 = Athlete(name='Test Athlete')
        test_athlete_1.save()
        test_date_1 = timezone.now() - datetime.timedelta(days=1)
        test_activity_1 = Activity(athlete=test_athlete_1, sport='test_sport', description='test_description',
                                   date=test_date_1)
        test_activity_1.save()
        feedback_description = 'test_feedback'
        test_feedback_1 = ActivityFeedback(activity=test_activity_1,description=feedback_description)
        test_feedback_1.save()
        self.assertEqual(test_activity_1.last_feedback(), feedback_description)