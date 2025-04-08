from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from bson import ObjectId

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create test users
        users = [
            User(email='user1@example.com', name='User One', password='password1'),
            User(email='user2@example.com', name='User Two', password='password2'),
            User(email='user3@example.com', name='User Three', password='password3'),
        ]
        User.objects.bulk_create(users)

        # Create test teams
        teams = [
            Team(name='Team Alpha', members=['user1@example.com', 'user2@example.com']),
            Team(name='Team Beta', members=['user3@example.com']),
        ]
        Team.objects.bulk_create(teams)

        # Create test activities
        activities = [
            Activity(user='user1@example.com', type='Running', duration=30),
            Activity(user='user2@example.com', type='Cycling', duration=60),
            Activity(user='user3@example.com', type='Swimming', duration=45),
        ]
        Activity.objects.bulk_create(activities)

        # Create test leaderboard entries
        leaderboard_entries = [
            Leaderboard(team='Team Alpha', points=100),
            Leaderboard(team='Team Beta', points=80),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create test workouts
        workouts = [
            Workout(name='Morning Run', description='A 5km run to start the day'),
            Workout(name='Evening Swim', description='A relaxing swim session'),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
