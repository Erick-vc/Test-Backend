from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RoutineViewSet, ExerciseViewSet, RegisterUserAPIView, AssignExercisesAPIView, CustomLoginView

router = DefaultRouter()
router.register('routines', RoutineViewSet)
router.register('exercises', ExerciseViewSet)

urlpatterns = [
    path('assign-exercises/', AssignExercisesAPIView.as_view()),
    path('auth/register/', RegisterUserAPIView.as_view(), name='register'),
    path('auth/login/', CustomLoginView.as_view(), name='login'),
    path('', include(router.urls)),
]
