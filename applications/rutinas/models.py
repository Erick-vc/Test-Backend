from django.contrib.auth.models import User
from django.db import models

class Exercise(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Routine(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    days = models.CharField(max_length=100) 
    time = models.TimeField()

    def __str__(self):
        return f"{self.name} - {self.user.username}"

class RoutineExercise(models.Model):
    routine = models.ForeignKey(Routine, on_delete=models.CASCADE, related_name='routine_exercises')
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
