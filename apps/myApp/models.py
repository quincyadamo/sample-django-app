from __future__ import unicode_literals
from django.db import models
import bcrypt
import datetime

# Create your models here.

class TripManager(models.Manager):
    def add(self, form_data, user_id):
        error_list = []
        is_valid = True
        today = datetime.datetime.today()

        if len(form_data['destination']) == 0:
            error_list.append("Please add a destination")
            is_valid = False
        if len(form_data['description']) == 0:
            error_list.append("Please add a description")
            is_valid = False

        try:
            from_date = datetime.datetime.strptime(form_data['from_date'], '%m/%d/%Y')
        except ValueError:
            error_list.append("Please enter a valid from date")
            is_valid = False

        try:
            to_date = datetime.datetime.strptime(form_data['to_date'], '%m/%d/%Y')
        except ValueError:
            error_list.append("Please enter a valid to date")
            is_valid = False

        if from_date < today or to_date < today:
            error_list.append("All dates must be in the future")
            is_valid = False

        if to_date < from_date:
            error_list.append("From date must be before to date")
            is_valid = False

        if is_valid:

            # add trip data with one to many user as the 'planner'
            new_trip = self.create(destination = form_data['destination'], description = form_data['description'], to_date = to_date, from_date = from_date, user_id = user_id)

            # add user to the many to many table
            new_trip.users.add(user_id)

            return (is_valid, new_trip)
        else:
            return (is_valid, error_list)

        return true

    def join(self, trip_id, user_id):
        trip = Trip.objects.get(id=trip_id)
        if trip:
            trip.users.add(user_id)
            return trip
        else:
            return False

class UserManager(models.Manager):
    def register(self, form_data):
        error_list = []
        is_valid = True

        if len(form_data['name']) < 3:
            error_list.append("Name must be 3 or more characters long!")
            is_valid = False
        if len(form_data['username']) < 3:
            error_list.append("Username must be 3 or more characters long!")
            is_valid = False
        if len(form_data['password']) < 8:
            error_list.append("Password must be at least 8 or more characters long!")
            is_valid = False
        if form_data['password'] != form_data['password_confirm']:
            error_list.append("Passwords do not match!")
            is_valid = False
        if User.objects.filter(username = form_data['username']):
            error_list.append("This Username already exists!")
            is_valid = False

        if is_valid:
            hashed_password = bcrypt.hashpw(form_data['password'].encode(), bcrypt.gensalt())
            new_user = self.create(name = form_data['name'], username = form_data['username'], pw_hash = hashed_password)
            return (is_valid, new_user)
        else:
            return (is_valid, error_list)

    def login(self, form_data):
        error_list = []

        if len(form_data['username']) == 0:
            error_list.append("Please enter a username")

        if len(form_data['password']) == 0:
            error_list.append("Please enter a password")

        user = User.objects.filter(username = form_data['username'])

        if user:
            user = user[0]
            if bcrypt.checkpw(form_data['password'].encode(), user.pw_hash.encode()):
                # Returning user object to views
                return (True, user)
        else:
            error_list.append("Username or password is incorrect")

        return (False, error_list)


class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    pw_hash = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Trip(models.Model):
    destination = models.CharField(max_length=255)
    description = models.TextField()
    to_date = models.DateTimeField()
    from_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    users = models.ManyToManyField(User, related_name="all_trips")
    user = models.ForeignKey(User, related_name="trip")
    objects = TripManager()
