from django.contrib import admin
from .models import Exercise, Routine, RoutineExercise


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    ordering = ('name',)


class RoutineExerciseInline(admin.TabularInline):
    model = RoutineExercise
    extra = 1
    autocomplete_fields = ['exercise']
    verbose_name = "Ejercicio en rutina"
    verbose_name_plural = "Ejercicios en esta rutina"


@admin.register(Routine)
class RoutineAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user', 'days', 'time')
    list_filter = ('days', 'user')
    search_fields = ('name', 'user__username')
    ordering = ('user', 'name')
    autocomplete_fields = ['user']
    inlines = [RoutineExerciseInline]


@admin.register(RoutineExercise)
class RoutineExerciseAdmin(admin.ModelAdmin):
    list_display = ('id', 'routine', 'exercise')
    list_filter = ('routine', 'exercise')
    search_fields = ('routine__name', 'exercise__name', 'routine__user__username')
    autocomplete_fields = ['routine', 'exercise']
    ordering = ('routine',)
