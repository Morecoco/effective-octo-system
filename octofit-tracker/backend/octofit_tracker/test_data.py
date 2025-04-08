# Test data for octofit_db

def get_test_data():
    return {
        "users": [
            {"email": "user1@example.com", "name": "User One", "password": "password1"},
            {"email": "user2@example.com", "name": "User Two", "password": "password2"},
            {"email": "user3@example.com", "name": "User Three", "password": "password3"}
        ],
        "teams": [
            {"name": "Team Alpha", "members": ["user1@example.com", "user2@example.com"]},
            {"name": "Team Beta", "members": ["user3@example.com"]}
        ],
        "activities": [
            {"user": "user1@example.com", "type": "Running", "duration": 30},
            {"user": "user2@example.com", "type": "Cycling", "duration": 60},
            {"user": "user3@example.com", "type": "Swimming", "duration": 45}
        ],
        "leaderboard": [
            {"team": "Team Alpha", "points": 100},
            {"team": "Team Beta", "points": 80}
        ],
        "workouts": [
            {"name": "Morning Run", "description": "A 5km run to start the day"},
            {"name": "Evening Swim", "description": "A relaxing swim session"}
        ]
    }
