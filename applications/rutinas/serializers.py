from rest_framework import serializers
from .models import Exercise, Routine, RoutineExercise
from django.contrib.auth.models import User

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'

class RoutineExerciseSerializer(serializers.ModelSerializer):
    exercise = ExerciseSerializer()

    class Meta:
        model = RoutineExercise
        fields = ['id', 'exercise']

class RoutineSerializer(serializers.ModelSerializer):
    routine_exercises = RoutineExerciseSerializer(many=True, read_only=True)

    class Meta:
        model = Routine
        fields = ['id', 'name', 'days', 'time', 'routine_exercises']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password']

    def create(self, validated_data):
        user = User(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user