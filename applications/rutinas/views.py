from rest_framework import generics, viewsets, permissions
from .models import Routine, Exercise, RoutineExercise
from .serializers import RoutineSerializer, ExerciseSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

class RoutineViewSet(viewsets.ModelViewSet):
    queryset = Routine.objects.all()
    serializer_class = RoutineSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False, methods=['get'], url_path='user/(?P<user_id>[^/.]+)')
    def routines_by_user(self, request, user_id=None):
        routines = self.queryset.filter(user_id=user_id)
        serializer = self.get_serializer(routines, many=True)
        return Response(serializer.data)


class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    permission_classes = [permissions.IsAuthenticated]

class AssignExercisesAPIView(generics.CreateAPIView):
    def post(self, request):
        routine_id = request.data.get('routine_id')
        exercise_ids = request.data.get('exercise_ids', [])
        for ex_id in exercise_ids:
            RoutineExercise.objects.create(routine_id=routine_id, exercise_id=ex_id)
        return Response({"status": "exercises assigned"})


class RegisterUserAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key, "user_id": user.id, "username": user.username})
        return Response(serializer.errors, status=400)

class CustomLoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({
            "token": token.key,
            "user_id": token.user_id,
            "username": token.user.username
        })